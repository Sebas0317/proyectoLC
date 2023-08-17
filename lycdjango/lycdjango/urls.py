from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings
from core import views
from core import views as core_views
from productos import views as productos_views

urlpatterns = [
    path('', views.home, name="home"),
    path('product-detail/<int:producto_id>/', core_views.product_detail, name='product_detail'),
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
    
    path('add_to_cart_home/<int:product_id>/', core_views.add_to_cart_home, name='add_to_cart_home'),
    
    path('remove_from_cart/<int:product_id>/', core_views.remove_from_cart, name='remove_from_cart'),
    
    path('update_cart_quantity/', views.update_cart_quantity, name='update_cart_quantity'),



    # """
    


    #     espacio reservado para futuros cambios


    # """
    #app contacto
    path('contacto/', include('contact.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)