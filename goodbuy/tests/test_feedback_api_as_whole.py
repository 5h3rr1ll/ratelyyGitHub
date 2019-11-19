from django.test import TestCase
from goodbuyDatabase.models import Product, Brand
import requests, re

class TestFeedbackApi(TestCase):
    def setUp(self):
        self.ean_code_in_db = '2000423339488'
        self.ean_code_not_in_db = '4000582185399'

        self.brand_obj = Brand.objects.create(
            name='Coca Cola'
        )
        self.product_obj = Product.objects.create(
            name='Coca Cola Light',
            code=self.ean_code_in_db,
            brand=Brand.objects.get(name='Coca Cola')
        )

    def test_feedback_ean_in_db_is_in_big_ten(self):
        response = self.request_api(self.ean_code_in_db)
        self.assertEqual(response, ['"is big ten": "True"'])

    def test_feedback_ean_not_in_db_is_in_big_ten(self):
        response = self.request_api(self.ean_code_not_in_db)
        self.assertEqual(response, ['"is big ten": "We don\'t know"'])

    def request_api(self, ean):
        response = requests.get('http://127.0.0.1:8000/feedback/%s/' %ean)
        print("response-------",response.text)
        is_not_in_big_ten = re.findall('"is big ten": "We don\'t know"', response.text)
        if is_not_in_big_ten == []:
            is_in_big_ten = re.findall('"is big ten": "True"', response.text)
            print("is in big ten", is_in_big_ten)
            return is_in_big_ten
        else:
            print("is not in big ten", is_not_in_big_ten)
            return is_not_in_big_ten



