from django.contrib import admin
from .models import Producto, Especificacion, TipoProducto, Comentario

class EspecificacionInline(admin.TabularInline):
    model = Especificacion

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'cantidad_disponible', 'fecha_carga', 'fecha_actualizacion', 'tipo')
    list_filter = ('precio', 'cantidad_disponible', 'fecha_carga', 'fecha_actualizacion', 'tipo')
    search_fields = ('nombre', 'tipo__nombre')
    list_editable = ('nombre', 'precio', 'cantidad_disponible', 'tipo')
    inlines = [EspecificacionInline]

    def get_tipo(self, obj):
        return obj.tipo.nombre if obj.tipo else None

    get_tipo.short_description = 'Tipo'  # Cambia el nombre de la columna para mostrar el tipo en el admin

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Comentario)
class comentarios(admin.ModelAdmin):
    list_display = ('autor','texto')

admin.site.register(TipoProducto, TipoProductoAdmin)
