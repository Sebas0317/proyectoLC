from django.urls import path
from . import views

urlpatterns = [
    path('pedido/', views.pedidos, name="pedidos_view"),
    
]