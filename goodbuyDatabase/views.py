from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DetailView, DeleteView
from django.http import HttpResponse, JsonResponse

from .forms import AddNewProductForm
from .models import Corporation, Brand, Product, CategoryOfProduct
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt

import requests
import json


def create_product(request):
    if request.method == "POST" and request.is_ajax():
        form = AddNewProductForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        image = request.POST["image"].replace("C:\\fakepath\\","product_image/")
        print("Image path:",image)
        if form.is_valid():
            print(request.POST)
            name = request.POST["name"]
            code = request.POST["code"]
            # TODO: use get_or_create() to add Brand or corporation
            # product.name = request.POST["name"]

            Product.objects.create(
                name = name,
                code = code,
                image = image,
            )
        else:
            print("\n!!! error While creating Product !!!\n")
        return HttpResponse("")
    else:
        print("\n!!! error While creating Product !!!\n")
    return HttpResponse("")

@login_required
def add_product(request, code):
    if request.method == "POST":
        form = AddNewProductForm(request.POST, request.FILES)

        if form.is_valid():
            '''commit=False allows you to modify the resulting object before it
            is actually saved to the database. Source:
            https://stackoverflow.com/questions/2218930/django-save-user-id-with-model-save?noredirect=1&lq=1'''
            product = form.save(commit=False)
            product.added_by = request.user
            if request.user.groups.filter(name="ProductGroup").exists():
                product.checked = True
                product.checked_by = request.user
                product.save()
                return redirect("/code_scanner/")
            else:
                product.checked = False
                product.save()
                return redirect("/code_scanner/")
        return render_to_response('goodbuyDatabase/add_product.html', {'form': form})
    else:
        try:
            product = Product.objects.get(code=code)
            product.scanned_counter += 1
            product.save()
            args = {
                "product":product,
            }
            return render(request,"goodbuyDatabase/product_already_exists.html",args)
        except Exception as e:
            print("type error: " + str(e))
            form = AddNewProductForm(initial={"code":code})
            args = {
                "form":form,
                "error":e,
                }
            return render(request, "goodbuyDatabase/add_product.html", args)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = [
        "name","code","image","brand","corporation","main_category",
        "sub_category","certificate",
        ]

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_staff == post.added_by.is_staff:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = "/goodbuyDatabase/list_all/"

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

def product_list(request):
    products = Product.objects.all()
    return render(
        request,
        "goodbuyDatabase/product_list.html",
        { "products":products })

def show_list_of_codes(request, list, *args, **kwargs):
    if request.method == "POST":
        form = AddNewProductForm(request.POST, request.FILES)
        if form.is_valid():
            '''
            commit=False allows you to modify the resulting object before it
            is actually saved to the database. Source:
            https://stackoverflow.com/questions/2218930/django-save-user-id-with-model-save?noredirect=1&lq=1
            '''
            product = form.save(commit=False)
            product.added_by = request.user
            if request.user.groups.filter(name="ProductGroup").exists():
                product.checked = True
                product.checked_by = request.user
                product.save()
                return redirect("/code_scanner/")
            else:
                product.checked = False
                product.save()
    else:
        single_codes = list.split(",")
        product_in_db = []
        product_not_in_db = []

        for code in single_codes:
            try:
                product = Product.objects.get(code=code)
                product_in_db.append(product)
            except:
                form = AddNewProductForm(initial={"code":code})
                product_not_in_db.append(form)

        args = {
            "allready_in_db":product_in_db,
            "product_not_in_db":product_not_in_db,
            }
        return render(request, "goodbuyDatabase/list_of_product_codes.html", args)

def receive_code(request, code):
    return HttpResponse(status=204)

class ProductDetailView(DetailView):
    model = Product

def is_big_ten(request, brandname):
    big_ten = ["Unilever","Nestlé","Coca-Cola","Kellog's","MARS","PEPSICO","Mondelez","General Mills","Associated British Foods plc","DANONE"]
    answer = { "in big ten" : brandname in big_ten }
    return JsonResponse(answer)

def is_in_own_database(request, code):
    return HttpResponse(str(Product.objects.filter(code=code).exists()))

def instant_feedback(request, code):

    # first check if the product is our own databse
    if Product.objects.filter(code=code).exists():
        args = {
            "product" : Product.objects.get(code=code)
            }
        return render(request, "goodbuyDatabase/product_detail.html", args)
    else:
        scraped_product = requests.get(f"http://127.0.0.1:8000/scraper/{code}").json()

    print("\n Hier is das Product:", scraped_product)

    if Brand.objects.filter(name=scraped_product["brand"]).exists() and CategoryOfProduct.objects.filter(name=scraped_product["product_category"]).exists():
        product = Product(
        name=scraped_product["name"],
        code=scraped_product["code"],
        brand=Brand.objects.get(name=scraped_product["brand"]),
        product_category=CategoryOfProduct.objects.get(name=scraped_product["product_category"]),
        scraped_image = scraped_product["scraped_image"],
        )
        product.save()
        is_in_one_of_big_ten(product.brand)
    else:
        category = CategoryOfProduct(name=scraped_product["product_category"])
        category.save()

        product = Product(
        name=scraped_product["name"],
        code=scraped_product["code"],
        brand=Brand.objects.get(name=scraped_product["brand"]),
        product_category=CategoryOfProduct.objects.get(name=scraped_product["product_category"]),
        scraped_image = scraped_product["scraped_image"],
        )
        product.save()
    if CategoryOfProduct.objects.filter(name=scraped_product["product_category"]).exists():

            brand = Brand(name=scraped_product["brand"])
            brand.save()
            product = Product(
                name=scraped_product["name"],
                code=scraped_product["code"],
                brand=Brand.objects.get(name=scraped_product["brand"]),
                product_category=CategoryOfProduct.objects.get(name=scraped_product["product_category"]),
                scraped_image = scraped_product["scraped_image"],
                )
            product.save()
    else:
        category = CategoryOfProduct(name=scraped_product["product_category"])
        category.save()
        product = Product(
            name=scraped_product["name"],
            code=scraped_product["code"],
            brand=Brand.objects.get(name=scraped_product["brand"]),
            product_category=CategoryOfProduct.objects.get(name=scraped_product["product_category"]),
            scraped_image = scraped_product["scraped_image"],
            )
        product.save()

        args = {
            "one_of_the_big_ten" : is_in_one_of_big_ten(scraped_product["brand"])
        }
        return render(request, "goodbuyDatabase/instant_feedback.html", args)

def feedback(request, code):
    print("In feedback")
    if Product.objects.filter(code=code).exists():
        print("in if")
        product_object = Product.objects.get(code=code)
        print(product_object)
        try:
            is_big_ten = requests.get(f"https://dev-goodbuy.herokuapp.com/isbigten/{product_object.brand}/")
            print("In Try is big ten:", is_big_ten)
        except Exception as e:
            print("\n request ERROR:", str(e))
        product_serialized = serializers.serialize("json", [product_object,])
        print(product_serialized)

        return HttpResponse(f"[{is_big_ten.text},{product_serialized}]")

@csrf_exempt
def endpoint_save_product(request):
    if request.method == "POST":
        product = json.loads(request.body.decode("utf-8"))
        Brand.objects.get_or_create(name=product["brand"])
        CategoryOfProduct.objects.get_or_create(name=product["product_category"])
        Product.objects.get_or_create(
            code=product["code"],
            name=product["name"],
            brand=Brand.objects.get(name=product["brand"]),
            product_category=CategoryOfProduct.objects.get(name=product["product_category"]),
            scraped_image=product["scraped_image"],
            )
        print("\n Request Body:", product["code"])
    else:
        print("ELSE!")
    return HttpResponse("")

@csrf_exempt
def endpoint_save_brand(request):
    if request.method == "POST":
        request = json.loads(request.body.decode("utf-8"))
        Brand.objects.get_or_create(name=request["brand"])
        print(f"Brand {request['brand']} saved.")
    else:
        print("ELSE!")
    return HttpResponse("")

@csrf_exempt
def endpoint_save_corporation(request):
    if request.method == "POST":
        request = json.loads(request.body.decode("utf-8"))
        Corporation.objects.get_or_create(name=request["corporation"])
        print(f"Corporation {request['corporation']} saved.")
    else:
        print("ELSE!")
    return HttpResponse("")
