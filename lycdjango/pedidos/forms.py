from django import forms

class DireccionEnvioForm(forms.Form):
    nombres_form = forms.CharField(label='Nombres', max_length=100)
    correo = forms.EmailField(label='Correo')
    numero_telefono = forms.CharField(label='Numero de Telefono', max_length=15)
    direccion = forms.CharField(label='Direccion', max_length=200)
