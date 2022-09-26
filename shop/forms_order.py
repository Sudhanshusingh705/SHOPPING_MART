from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['products_id', 'user', 'total', 'discount', 'tax', 'price', 'address', 'order_id', 'pincode']