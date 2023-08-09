from django.contrib import admin
from .models import GastosEnvio

@admin.register(GastosEnvio)
class GastosEnvioAdmin(admin.ModelAdmin):
    list_display = ('monto',)  # Campo que se mostrará en la lista de registros
