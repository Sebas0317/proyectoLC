from django import forms
from .models import Comentario 

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['reviewer_name', 'email', 'text']




class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']  # Debe incluir el campo 'texto' en los campos del formulario

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields['texto'].widget = forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu comentario aquí'})  # Agrega el widget Textarea y un placeholder opcional

    def clean_texto(self):
        texto = self.cleaned_data.get('texto')
        # Agrega tus propias validaciones aquí si es necesario
        return texto
