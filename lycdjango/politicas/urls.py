from django.urls import path
from . import views

urlpatterns = [
    path('politica-privacidad/', views.privacidad, name='politica-privacidad'),
    path('sobre-nosotros/', views.aboutme, name='sobre-nosotros'),
    path('terminos-condiciones/', views.Terminos, name='terminos-condiciones'),
    path('politica-pagos/', views.Politicapago, name='politica-pagos'),
    path('politica-envios/', views.Politicaenvio, name='politica-envios'),
    path('politica-devoluciones/', views.Politicadev, name='politica-devoluciones'),
    # path('politica-terminosycondiciones/', views.terminos, name='politica-tt_cc'),
    # path('politica-pagos/', views.pagos, name='politica-pagos'),
]