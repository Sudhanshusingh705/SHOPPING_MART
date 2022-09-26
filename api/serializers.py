from rest_framework import serializers

from shop.models import Product, Company, Order
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
