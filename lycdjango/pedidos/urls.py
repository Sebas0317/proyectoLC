from django.urls import path
from . import views

urlpatterns = [
    path('pedido/', views.pedidos, name="pedidos_view"),
    path('checkout/', views.checkout, name="checkout"),
    # path('enviar_email/', views.send_email, name='enviar_email'),
]