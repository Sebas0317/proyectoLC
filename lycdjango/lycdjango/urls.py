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
from django.urls import path, include
from django.conf.urls.static import static, settings
from core import views
from core import views as core_views
from productos import views as productos_views

urlpatterns = [
    path('', views.home, name="home"),
    path('product-detail/', views.product_detail, name="product-detail"),
    path('product-detail/<int:producto_id>/',views.product_detail, name='product-detail'),
    path('product_list/', productos_views.product_list, name='product_list'),
    path('checkout/', views.checkout, name="checkout"),
    path('my-account/', core_views.myaccount, name="my-account"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('contact/', views.contact, name="contact"),
    path('user_admin/', views.admin, name="admin"),
    path('regis/', views.regis, name="regis"),
    path('admin/', admin.site.urls),
    
    
    path('cart/', core_views.product_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', core_views.add_to_cart, name='add_to_cart'),
    path('add_to_cart_product_list/<int:product_id>/', core_views.add_to_cart_product_list, name='add_to_cart_product_list'),
    path('remove_from_cart/<int:product_id>/', core_views.remove_from_cart, name='remove_from_cart'),

    """
    


        espacio reservado para futuros cambios




    """
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)