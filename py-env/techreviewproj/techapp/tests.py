from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django import forms
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

class ProductFormTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='user1', password='P@ssw0rd1')


#without form here, tests don't work :(

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model=ProductType
        fields='__all__'

# tests for form

class ProductType_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        form=ProductTypeForm(data={'typename': "type1", 'typedescription' : "some type"})
        self.assertTrue(form.is_valid())

    def test_typeform_minus_descript(self):
        form=ProductTypeForm(data={'typename': "type1"})
        self.assertTrue(form.is_valid())

    def test_typeform_empty(self):
        form=ProductTypeForm(data={'typename': ""})
        self.assertFalse(form.is_valid())