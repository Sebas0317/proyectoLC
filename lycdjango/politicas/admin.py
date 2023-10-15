from django import forms 
from django.contrib import admin
from django.core.files.images import get_image_dimensions
from django.utils.html import format_html
from .models import GastosEnvio, Cupon, CorreoEmpresa, BrandImage, Polprivacidad, Acercade, Terminos, Polpago, Polenvio, Poldevoluiones, Copyright

# Define un formulario personalizado para BrandImage con validación de dimensiones
class BrandImageForm(forms.ModelForm):
    class Meta:
        model = BrandImage
        fields = '__all__'

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Obtiene las dimensiones de la imagen
            width, height = get_image_dimensions(image)
            
            # Verifica las dimensiones del archivo
            if width != 150 or height != 80:
                raise forms.ValidationError('La imagen debe tener dimensiones de 150x80 píxeles.')

        return image

@admin.register(GastosEnvio)
class GastosEnvioAdmin(admin.ModelAdmin):
    list_display = ('monto',)

@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descuento')

@admin.register(CorreoEmpresa)
class CorreoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('direccion','correo','telefono')

@admin.register(BrandImage)
class BrandImageAdmin(admin.ModelAdmin):
    list_display = ('display_image',)

    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
    
    display_image.short_description = 'Image'
    form = BrandImageForm  # Usa el formulario personalizado

# @admin.register(Polprivacidad)
# class politica_privacidad(admin.ModelAdmin):
#     list_display = ('titulo', '')

@admin.register(Acercade)
class sobre_nosotros(admin.ModelAdmin):
    list_display = ('titulo', 'contenido')

@admin.register(Terminos)
class Terminos_condiciones(admin.ModelAdmin):
    list_display = ('titulo', 'contenido')

@admin.register(Polpago)
class politica_pago(admin.ModelAdmin):
    list_display = ('titulo', 'contenido')

@admin.register(Polenvio)
class politica_envio(admin.ModelAdmin):
    list_display = ('titulo', 'contenido')

@admin.register(Poldevoluiones)
class politica_devolucion(admin.ModelAdmin):
    list_display = ('titulo', 'contenido')
    

class CopyrightAdmin(admin.ModelAdmin):
    list_display = ('frase',)

admin.site.register(Copyright, CopyrightAdmin)



