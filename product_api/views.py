from django.shortcuts import render

from rest_framework import status, viewsets, filters

from product_api.models import Category, Supplier, Product, Customer, Order
from product_api.serializers import CategorySerializer, ProductSerializer, SupplierSerializer, CustomerSerializer, OrderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
        Handles a category instance
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class SupplierViewSet(viewsets.ModelViewSet):
    """
        Handles a supplier instance
    """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class ProductViewSet(viewsets.ModelViewSet):
    """
        Handles a product instance
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class CustomerViewSet(viewsets.ModelViewSet):
    """
        Handles a customer instance
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class OrderViewSet(viewsets.ModelViewSet):
    """
        Handles an order instance
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('order_id',)