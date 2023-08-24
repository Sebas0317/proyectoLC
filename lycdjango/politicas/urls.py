from django.urls import path
from . import views

urlpatterns = [
    path('politica-privacidad/', views.privacidad, name='politica-privacidad'),
    path('sobre-nosotros/', views.aboutme, name='sobre-nosotros'),
    path('terminos-condiciones/', views.terminos, name='terminos-condiciones'),
    path('politica-pagos/', views.politica_pago, name='politica-pagos'),
    path('politica-envios/', views.politica_envio, name='politica-envios'),
    path('politica-devoluciones/', views.politica_devolucion, name='politica-devoluciones'),
]
