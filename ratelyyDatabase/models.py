from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User



class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    code = models.CharField(unique=True, max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    class Meta:
        managed = True
        db_table = "countries"
        verbose_name_plural = "Countries"
        ordering = ("name","id",)

    def __str__(self):
        return self.name


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    country = models.ForeignKey(Country, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = "stores"
        ordering = ("name","id",)


class Concern(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, verbose_name="Concern Name", unique=True)
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    origin = models.ForeignKey(Country, models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'concerns'
        ordering = ("name","id",)

    def __str__(self):
        return self.name


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    humans = models.IntegerField(
        validators=[MinValueValidator(1),
        MaxValueValidator(10)],
        null=True,
        blank=True,
        )
    humans_description = models.TextField(null=True,blank=True,)
    environment = models.IntegerField(validators=[MinValueValidator(1),
        MaxValueValidator(10)],
        null=True,
        blank=True,
        )
    environment_description = models.TextField(null=True,blank=True,)
    animals = models.IntegerField(validators=[MinValueValidator(1),
        MaxValueValidator(10)],
        null=True,
        blank=True,
        )
    animals_description = models.TextField(null=True,blank=True,)
    concern = models.ForeignKey(
        Concern, models.SET_NULL,
        null=True,blank=True,
        unique=True
        )

    class Meta:
        managed = True
        db_table = "ratings"
        ordering = ("concern","id",)

    def __str__(self):
        return self.concern.name


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    concern = models.ForeignKey(Concern, models.SET_NULL, db_column="concern", null=True, blank=True)
    origin = models.ForeignKey(Country, models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'companies'
        ordering = ("name","id",)
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,)
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    company = models.ForeignKey(Company, models.SET_NULL, null=True, blank=True)
    concern = models.ForeignKey(Concern, models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'brands'
        ordering = ("name","id",)


    def __str__(self):
        return self.name


class MainCategoryOfProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "main_category_of_products"

    def __str__(self):
        return self.name


class SubCategoryOfProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    main_category = models.ForeignKey(MainCategoryOfProduct, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "sub_category_of_products"

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45,verbose_name="Product Name")
    logo = models.URLField(null=True, blank=True)
    wiki = models.URLField(null=True, blank=True)
    code = models.CharField(null=True,blank=True,unique=True, max_length=13)
    image = models.URLField(null=True, blank=True, max_length=300)
    brand = models.ForeignKey(Brand, models.SET_NULL, null=True, blank=True)
    concern = models.ForeignKey(Concern, models.SET_NULL, null=True, blank=True)
    main_category = models.ForeignKey(MainCategoryOfProduct, models.SET_NULL, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategoryOfProduct, models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stat_counter = models.IntegerField(null=True, blank=True)
    added_by = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'products'
        ordering = ("name","id",)

    def __str__(self):
        return self.name


class OrganicCertification(models.Model):
    pass


class ProductPriceInStore(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'product_price_in_store'

    def __str__(self):
        return str(self.price)