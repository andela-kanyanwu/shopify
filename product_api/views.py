from django.shortcuts import render
from django.http import Http404

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from product_api.models import Category, Supplier, Product, Customer, Order
from product_api.serializers import CategorySerializer, ProductSerializer, SupplierSerializer, CustomerSerializer, OrderSerializer

# class ProductList(APIView):
#     """
#         List all products, or create a new product
#     """
#     serializer_class = ProductSerializer

#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ModelViewSet):
    """
        Handles a category instance
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class SupplierViewSet(viewsets.ModelViewSet):
    """
        Handles a supplier instance
    """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    """
        Handles a product instance
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CustomerViewSet(viewsets.ModelViewSet):
    """
        Handles a customer instance
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    """
        Handles a customer instance
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()