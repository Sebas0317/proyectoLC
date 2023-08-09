from django.contrib import admin
from .models import GastosEnvio, Cupon, CorreoEmpresa

@admin.register(GastosEnvio)
class GastosEnvioAdmin(admin.ModelAdmin):
    list_display = ('monto',)

@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descuento')

@admin.register(CorreoEmpresa)
class CorreoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('correo',)  # Cambia 'Correo' por 'correo' para que coincida con el nombre del campo en el modelo

