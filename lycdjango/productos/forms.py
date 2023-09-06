from django import forms
from .models import Comentario 

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['reviewer_name', 'email', 'text']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']  # Los campos que deseas incluir en el formulario

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields['texto'].widget = forms.Textarea(attrs={'rows': 4})  # Opcional: Cambia el widget del campo de texto

    def clean_texto(self):
        texto = self.cleaned_data.get('texto')
        # Agrega tus propias validaciones aquí si es necesario
        return texto
