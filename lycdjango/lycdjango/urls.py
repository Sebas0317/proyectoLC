"""
URL configuration for lycdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from core import views
from core import views as core_views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('product-detail/', views.productdetail, name="product-detail"),
    path('product-list/', views.productlist, name="product-list"),
    path('checkout/', views.checkout, name="checkout"),
    path('my-account/', core_views.myaccount, name="my-account"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('contact/', views.contact, name="contact"),
    path('admin/', views.admin, name="admin"),
    path('regis/', views.regis, name="regis"),
    path('admin/', admin.site.urls),
]