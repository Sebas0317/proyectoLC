from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings
from core import views as core_views
from productos import views as productos_views
from pedidos import views as pedidos_views

urlpatterns = [
    # Vistas generales
    path('', core_views.home, name="home"),
  
    path('contact/', core_views.contact, name="contact"),
    path('user_admin/', core_views.admin, name="admin"),
    path('my-account/', core_views.myaccount, name="my-account"),
    
    path('pedido/', pedidos_views.pedidos, name="pedidos_view"),
    path('checkout/', pedidos_views.checkout, name="checkout"),
    
    # path('enviar_email/', pedidos_views.send_email, name='enviar_email'),
    
    # Detalles de productos
    path('product-detail/<int:producto_id>/', core_views.product_detail, name='product_detail'),

    # Listado de productos
    path('product_list/', productos_views.product_list, name='product_list'),
    path('comentarios/', productos_views.crear_comentario, name='comentarios'),

    # Carrito de compras
    path('cart/', core_views.product_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', core_views.add_to_cart, name='add_to_cart'),
    
    path('remove_from_cart/<int:product_id>/', core_views.remove_from_cart, name='remove_from_cart'),
    path('update_cart_quantity/', core_views.update_cart_quantity, name='update_cart_quantity'),
    
    path('move_to_cart/<int:product_id>/', core_views.move_to_cart, name='move_to_cart'),


    # Lista de deseos
    path('wishlist/', core_views.wish_cart, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', core_views.add_to_wish, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:product_id>/', core_views.remove_from_wish, name='remove_from_wishlist'),

    # Políticas y administración
    path('politicas/', include('politicas.urls')),
    path('admin/', admin.site.urls),

    # Registro y autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    #app contacto
    path('contacto/', include('contact.urls')),
]

# Rutas para archivos multimedia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
