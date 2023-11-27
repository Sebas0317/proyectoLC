from django.contrib import admin
from .models import Producto, Especificacion, TipoProducto, Comentario

class EspecificacionInline(admin.TabularInline):
    model = Especificacion
from django.contrib import admin
from .models import Producto, TipoProducto, Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'cantidad_disponible', 'fecha_carga', 'fecha_actualizacion', 'tipo')
    list_filter = ('precio', 'cantidad_disponible', 'fecha_carga', 'fecha_actualizacion', 'tipo')
    search_fields = ('nombre', 'tipo__nombre')
    list_editable = ('nombre', 'precio', 'cantidad_disponible', 'tipo')
    inlines = [ComentarioInline]

    def get_tipo(self, obj):
        return obj.tipo.nombre if obj.tipo else None

    get_tipo.short_description = 'Tipo'

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'contenido', 'fecha')  

