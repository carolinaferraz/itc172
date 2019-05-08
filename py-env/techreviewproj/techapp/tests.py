from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from .models import Product, ProductType, Review


# Create your tests here.

#tests for models

class TechTypeTest(TestCase):
    def test_string(self):
        type=ProductType(typename='laptop')
        self.assertEqual(str(type), type.typename)

    def test_table(self):
        self.assertEqual(str(ProductType._meta.db_table), 'producttype')

class ProductTest(TestCase):
    def setUp(self):
        self.type=ProductType(typename='tablet')
        self.prod = Product(productname='iPad', producttype=self.type, productprice=800.00)

    def test_string(self):
        self.assertEqual(str(self.prod), self.prod.productname)

    def test_type(self):
        self.assertEqual(str(self.prod.producttype), 'tablet')

    def test_discount(self):
        self.assertEqual(self.prod.memberdiscount(), 40.00)

#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_the_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

#not working :(
# class GetProductsTest(TestCase):
#     def setUp(self):
#         self.u=User.objects.create(username='myuser')
#         self.type=ProductType.objects.create(typename='laptop')
#         self.prod = Product.objects.create(productname='product1', producttype=self.type, user=self.u, productprice=500.00, productentrydate='2019-04-02', productdescription="a product")

#     def test_product_detail_success(self):
#         response = self.client.get(reverse('productdetails', args=(self.prod.id,)))
#         self.assertEqual(response.status_code, 200)