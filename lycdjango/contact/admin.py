from django.contrib import admin
from .models import Mensaje

class MensajeAdmin(admin.ModelAdmin):
    list_display = ('id','get_nombre', 'correo', 'view_asunto', 'mensaje', 'estado')
    list_filter = ('estado',)
    readonly_fields = ['view_asunto','correo','nombre','mensaje']

    fieldsets = [
        (None, {'fields': ['nombre', 'correo', 'view_asunto', 'mensaje', 'estado']}),
    ]

    def get_nombre(self, obj):
        return f"Mensaje de {obj.nombre}"
    get_nombre.short_description = 'Nombre'

    def view_asunto(self, obj):
        return obj.asunto
    view_asunto.admin_order_field = 'asunto'
    view_asunto.short_description = 'Asunto'

admin.site.register(Mensaje, MensajeAdmin)
