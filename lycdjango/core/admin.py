from django.contrib import admin
from .models import Comentario
from django import forms

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['nombre_comprador', 'comentario']
    search_fields = ['nombre_comprador', 'comentario']

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'imagen':
            kwargs['widget'] = forms.ClearableFileInput(attrs={'accept': 'image/*'})
            kwargs['help_text'] = 'La imagen debe tener al menos 200x200 píxeles.'
        return super().formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Comentario, ComentarioAdmin)
