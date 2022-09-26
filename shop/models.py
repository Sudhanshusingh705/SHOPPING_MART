from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Company(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    created_at = models.DateField(auto_now_add=True)
    logo = models.ImageField(upload_to='shop/images/company', blank= True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    company = models.ForeignKey(Company, on_delete = models.CASCADE, blank = True)
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_image = models.ImageField(upload_to='shop/images/product')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    
    order_id = models.CharField(max_length=200)
    products_id = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
    total = models.IntegerField()
    discount = models.IntegerField()
    status = models.CharField(max_length=100, blank=True, null=True)
    tax = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=1000)
    pincode = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.order_id