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
        """
            Ensure we get an empty list when no category object is available.
        """
        Category.objects.all().delete()
        data = []
        response = self.client.get('/categories/')
        self.assertEqual(response.data, data)

    def test_post_category(self):
        """
            Ensure we can create a category object.
        """
        data = {"id": 2, "name": "All", "description": "Available for everyone"}
        response = self.client.post('/categories/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_post_category_with_empty_field(self):
        """
            Ensure we cannot post category with empty field.
        """
        data = {"name": "", "description": ""}
        response = self.client.post('/categories/', data, format='json')
        self.assertEqual(response.data, {'name': ['This field may not be blank.'], 'description': ['This field may not be blank.']})

    def test_delete_category(self):
        """
            Ensure we can delete a category object.
        """
        data = {"id": 1, "name": "All", "description": "Available for everyone"}
        response = self.client.delete("/categories/1/")
        self.assertEqual(response.data, None)

    def test_put_category(self):
        """
            Ensure we can update a category object.
        """
        data = {"id": 1, "name": "All", "description": "Available for everyone"}
        response = self.client.put("/categories/1/", data, format='json')
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
        data = [{"url": "http://testserver/products/1/", "name": "soap", "description": "Best soap", "category": "http://testserver/categories/1/", "supplier": "http://testserver/suppliers/1/", "price_per_unit": 20, "size": "small", "colour": "white"}]

        response = self.client.get('/products/')
        self.assertEqual(response.data, data)

    def test_get_product_when_no_data_is_available(self):
        """
            Ensure we get an empty list when no product object is available.
        """
        Product.objects.all().delete()
        data = []
        response = self.client.get('/products/')
        self.assertEqual(response.data, data)

    def test_get_product_with_primary_key_that_does_not_exist(self):
        """
            Ensure we get a 'Not found' data for product with primary key that do not exist
        """
        data = {"detail": "Not found."}
        response = self.client.get('/products/3/')
        self.assertEqual(response.data, data)

    def test_post_product(self):
        """
            Ensure we can create a product object
        """
        Category.objects.create(name="All", description="Available for everyone")
        Supplier.objects.create(name="Djangs", address="32 Mac road", city="Lagos", country="Nigeria", email="djangs@yahoo.com", website="www.yahoo.com")
        data = {"url": "http://testserver/products/2/", "name": "soap", "description": "Best soap", "category": 'http://testserver/categories/2/', "supplier": "http://testserver/suppliers/2/", "price_per_unit": 20, "size": "small", "colour": "white"}
        response = self.client.post('/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_delete_product(self):
        """
            Ensure we can delete a product object.
        """
        data = {"url": "http://testserver/products/1/", "name": "soap", "description": "Best soap", "category": "http://testserver/categories/1/", "supplier": "http://testserver/suppliers/1/", "price_per_unit": 20, "size": "small", "colour": "white"}
        response = self.client.delete("/products/1/")
        self.assertEqual(response.data, None) 

    def test_delete_product_with_primary_key_that_does_not_exist(self):
        """
            Ensure we cannot delete a product with primary key that does not exist.
        """
        data = {"detail": "Not found."}
        response = self.client.delete("/products/4/")
        self.assertEqual(response.data, data)

    def test_put_product(self):
        """
            Ensure we can update a product object.
        """
        data = {"url": "http://testserver/products/1/", "name": "soap", "description": "Best soap", "category": "http://testserver/categories/1/", "supplier": "http://testserver/suppliers/1/", "price_per_unit": 20, "size": "small", "colour": "white"}
        response = self.client.put("/products/1/", data, format='json')
        self.assertEqual(response.data, data)


class OrderTest(APITestCase):
    def setUp(self):
        category_object = Category.objects.create(name="All", description="Available for everyone")
        supplier_object = Supplier.objects.create(name="Djangs", address="32 Mac road", city="Lagos", country="Nigeria", email="djangs@yahoo.com", website="www.yahoo.com")
        product_object = Product.objects.create(name="soap", description="Best soap", category=category_object, supplier=supplier_object, price_per_unit=20, size="small", colour="white")
        customer_object = Customer.objects.create(name="Mac", address="32 Mac road", city="Lagos", country="Nigeria")

        order = Order(order_id=1, date="2015-06-11T17:03:33Z", quantity_ordered=10, total_cost=200, customer=customer_object)
        order.save()
        order.product.add(product_object)

    def test_get_orders(self):
        """
            Ensure we can get all order objects.
        """
        data = [{'url': 'http://testserver/orders/1/', 'date': '2015-06-11T17:03:33Z', 'quantity_ordered': 10, 'total_cost': 200, 'customer': 'http://testserver/customers/1/', 'product': ['http://testserver/products/1/']}]
        response = self.client.get('/orders/')
        self.assertEqual(response.data, data)

    def test_post_orders(self):
        """
            Ensure we can create an order object.
        """
        data = {'url': 'http://testserver/orders/2/', 'date': '2015-07-11T17:03:33Z', 'quantity_ordered': 5, 'total_cost': 150, 'customer': 'http://testserver/customers/1/', 'product': ['http://testserver/products/1/']}

        response = self.client.post('/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_delete_order(self):
        """
            Ensure we can delete an order
        """
        data = [{'url': 'http://testserver/orders/1/', 'date': '2015-06-11T17:03:33Z', 'quantity_ordered': 10, 'total_cost': 200, 'customer': 'http://testserver/customers/1/', 'product': ['http://testserver/products/1/']}]
        response = self.client.delete('/orders/1/')
        self.assertEqual(response.data, None)
