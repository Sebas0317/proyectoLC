from django.urls import path
from . import views

urlpatterns = [
    path('politica-privacidad/', views.privacidad, name='politica-privacidad'),   
    # path('politica-terminosycondiciones/', views.terminos, name='politica-tt_cc'),
    # path('politica-pagos/', views.pagos, name='politica-pagos'),
]