from django.urls import path, include
from . import views

urlpatterns = [
    path('pedido/', views.pedidos, name="pedidos_view"),
    path('checkout/', views.checkout, name="checkout"),
    path('', include('lycdjango.urls')),
    # path('enviar_email/', views.send_email, name='enviar_email'),
]