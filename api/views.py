from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer, OrderSerializer
from shop.models import Product, Order

@api_view(['GET'])
def product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def order_details(request, id):

    if request.method == 'GET':
        order = Order.objects.filter(order_id=id)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
