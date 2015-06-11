from django.db import models


class Category(models.Model):
    """
        Handles information about category of the product
    """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, default="No description available")

    def __unicode__(self):
        return self.name

class Supplier(models.Model):
    """
        Handles information about the supplier of the product
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    """ 
        Handles information about the product 
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, default="No description available")
    category = models.ForeignKey(Category)
    supplier = models.ForeignKey(Supplier, blank=True)
    price_per_unit = models.PositiveIntegerField()
    size = models.CharField(max_length=100, blank=True)
    colour = models.CharField(max_length=30, blank=True)
   
    def __unicode__(self):
        return self.name

class Customer(models.Model):
    """
        Handles information about the customer that placed an order
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Order(models.Model):
    """
        Handles information about product orders 
    """
    order_id = models.AutoField(primary_key=True)
    product = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer)
    date = models.DateTimeField()
    quantity_ordered = models.PositiveIntegerField()
    total_cost = models.PositiveIntegerField()

    def __unicode__(self):
        return str(self.order_id)
