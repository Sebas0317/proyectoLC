from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']  # Asegúrate de que el campo 'contenido' esté aquí
        widgets = {
            'contenido': forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí'})
        }
