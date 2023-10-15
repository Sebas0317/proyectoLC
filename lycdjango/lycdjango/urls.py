from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings
from core import views as core_views
from productos import views as productos_views
from pedidos import views as pedidos_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # Vistas generales
     path('', core_views.home, name="home"),
  
    path('', include('contact.urls')),
    path('user_admin/', core_views.admin, name="admin"),
    path('my-account/', login_required(core_views.myaccount), name="my-account"),
    path('pedido/', login_required(pedidos_views.pedidos), name="pedidos_view"),
    path('checkout/', login_required(pedidos_views.checkout), name="checkout"),
    
    # path('enviar_email/', login_required(pedidos_views.send_email), name='enviar_email'),
    
    path('product-detail/<int:producto_id>/', login_required(core_views.product_detail), name='product_detail'),

    path('product_list/', login_required(productos_views.product_list), name='product_list'),
    path('comentarios/', login_required(productos_views.crear_comentario), name='comentarios'),

    path('cart/', login_required(core_views.product_cart), name='cart'),
    path('add_to_cart/<int:product_id>/', login_required(core_views.add_to_cart), name='add_to_cart'),
    
    path('remove_from_cart/<int:product_id>/', login_required(core_views.remove_from_cart), name='remove_from_cart'),
    path('update_cart_quantity/', login_required(core_views.update_cart_quantity), name='update_cart_quantity'),
    path('move_to_cart/<int:product_id>/', login_required(core_views.move_to_cart), name='move_to_cart'),

    path('wishlist/', login_required(core_views.wish_cart), name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', login_required(core_views.add_to_wish), name='add_to_wishlist'),
    path('remove_from_wishlist/<int:product_id>/', login_required(core_views.remove_from_wish), name='remove_from_wishlist'),

    path('politicas/', include('politicas.urls')),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    path('contacto/', include('contact.urls'))
]

# Rutas para archivos multimedia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
