from cgitb import text
from django import forms

class Contactoformulario(forms.Form):
    nombre = forms.CharField(label="nombre", required=True, widget=forms.TextInput(attrs={'placeholder':'escriba su nombre','class': 'form-control'}),min_length=3, max_length=100)
    correo=forms.CharField(label="correo electronico", required=True, widget=forms.EmailInput(attrs={'placeholder':'escriba su email','class': 'form-control'}),min_length=3, max_length=100)
    mensaje=forms.CharField(label="mensaje", required=True, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))