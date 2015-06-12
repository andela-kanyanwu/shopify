from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from product_api.models import Category, Supplier, Product, Customer, Order

class CategoryTest(APITestCase):
    def setUp(self):
        Category.objects.create(name="All", description="Available for everyone")

    def test_get_category(self):
        """
            Ensure we can get all category objects.
        """
        data = [{"id": 1, "name": "All", "description": "Available for everyone"}]
        response = self.client.get('/categories/')
        self.assertEqual(response.data, data)

    def test_get_category_when_no_data_is_available(self):
        Category.objects.all().delete()
        data = []
        response = self.client.get('/categories/')
        self.assertEqual(response.data, data)

    def test_post_category(self):
        """
            Ensure we can create a category objects.
        """
        data = {"id": 2, "name": "All", "description": "Available for everyone"}
        response = self.client.post('/categories/', data, format='json')
        self.assertEqual(response.data, data)


class ProductTest(APITestCase):
    def setUp(self):
        category_object = Category.objects.create(name="All", description="Available for everyone")
        supplier_object = Supplier.objects.create(name="Djangs", address="32 Mac road", city="Lagos", country="Nigeria", email="djangs@yahoo.com", website="www.yahoo.com")
        Product.objects.create(name="soap", description="Best soap", category=category_object, supplier=supplier_object, price_per_unit=20, size="small", colour="white")

    def test_get_product(self):
        """
            Ensure we can get all product objects.
        """
        data = [{"url": "http://testserver/products/1/", "name": "soap", "description": "Best soap", "category": 'http://testserver/categories/1/', "supplier": "http://testserver/suppliers/1/", "price_per_unit": 20, "size": "small", "colour": "white"}]

        response = self.client.get('/products/')
        self.assertEqual(response.data, data)
    