"""shopping_mart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
from shop import views as viewsshop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsshop.crud, name = "home"),
    path('category/<str:cat>', viewsshop.showcategory, name = "showcategory"),
    path('brands/<str:comp>', viewsshop.showcompany, name = "showcompany"),
    path('product/<str:product_id>', viewsshop.showproduct, name = "showproduct"),
    path('signup/', views.signup, name = "signup"),
    path('logout/', views.logout_request, name = "logout"),
    path('login/', views.login_request, name = "login"),
    path('account/', views.account, name = "account"),
    path('order/', viewsshop.order, name = "order"),
    path('api/', include('api.urls')),
    path('shop/', include('shop.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
