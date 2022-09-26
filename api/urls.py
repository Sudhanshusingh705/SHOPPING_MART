from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('order-id/<str:id>', views.order_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)