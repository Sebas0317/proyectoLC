from django import forms
from django.contrib import admin
from django.core.files.images import get_image_dimensions
from django.utils.html import format_html
from .models import GastosEnvio, Cupon, CorreoEmpresa, BrandImage

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
