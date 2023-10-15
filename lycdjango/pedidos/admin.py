from django.contrib import admin
from .models import PedidosOrden, PedidosByUser

class PedidosOrdenAdmin(admin.ModelAdmin):
    list_display = ['id_pedido',  'producto', 'cantidad', 'total', 'estado_pedido']
    readonly_fields = ['user', 'producto', 'cantidad', 'total', 'nombres', 'correo', 'direccion', 'numero_telefono', 'fecha_compra']

    actions = ['editar_pedido']

    def editar_pedido(self, request, queryset):
        # Habilitamos la edición de los campos readonly
        self.readonly_fields = []

        # Redirigimos a la página de edición de cada pedido seleccionado
        return queryset

    editar_pedido.short_description = "Editar Pedido"

    def save_model(self, request, obj, form, change):
        # Después de guardar, volvemos a poner los campos como solo lectura
        self.readonly_fields = ['user', 'producto', 'cantidad', 'total', 'nombres', 'correo', 'direccion', 'numero_telefono', 'fecha_compra']
        super().save_model(request, obj, form, change)
        
class PedidosByUserAdmin(admin.ModelAdmin):
    
    list_display = ['user']
 

admin.site.register(PedidosOrden, PedidosOrdenAdmin)
admin.site.register(PedidosByUser, PedidosByUserAdmin)
