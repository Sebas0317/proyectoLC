from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'correo', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo electrónico'}),
            'asunto': forms.TextInput(attrs={'placeholder': 'Ingresa el asunto'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí'}),
        }
