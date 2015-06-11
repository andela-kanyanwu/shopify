from django.forms import widgets
from rest_framework import serializers
from product_api.models import Category, Supplier, Product, Customer, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order