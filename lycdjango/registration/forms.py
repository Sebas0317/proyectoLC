from  django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class User_email(UserCreationForm): # seccion del correo
    email = forms.EmailField(required=True, help_text='requerido 254 caracteres maximo y debe ser un correo valido')

    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email", "password1", "password2")

    def clean_email(self): #validacion correo
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'el correo ya esta registrado, prueba otro')
        return email
    


