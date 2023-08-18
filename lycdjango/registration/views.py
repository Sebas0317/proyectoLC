from django.shortcuts import render
#from django.contrib.auth.models import User 
from .forms import User_email
from django.views.generic import CreateView
from django.urls import  reverse_lazy
from  django import forms
from django.views.generic import TemplateView
#from .forms import UserCreationForm

# Create your views here.


#----------------------------------------------------------------
class SignUpView(CreateView): #registro user
    form_class = User_email
    template_name = 'registration/signup.html'
    #success_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse_lazy('login') + '?register'   
        

    def get_form(self, form_class=None):
        form  = super (SignUpView, self).get_form()
        form.fields['first_name'].widget = forms.TextInput( attrs={'class': 'form-control mb-2', "placeholder": 'Nombres'})
        form.fields['last_name'].widget = forms.TextInput( attrs={'class': 'form-control mb-2', "placeholder": 'Apellidos'})
        form.fields['username'].widget = forms.TextInput( attrs={'class': 'form-control mb-2', "placeholder": 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput( attrs={'class': 'form-control mb-2', "placeholder": 'Correo electrónico'})
        form.fields['password1'].widget = forms.PasswordInput (attrs={'class':'form-control mb-2', "placeholder": 'Contraseña'}) 
        form.fields['password2'].widget = forms.PasswordInput (attrs={'class':'form-control mb-2', "placeholder": 'Repita la contraseña'})
        form.fields['username'].label = ''
        form.fields['first_name'].label = ''
        form.fields['last_name'].label = ''
        form.fields['email'].label = ''
        form.fields['password1'].label = ''
        form.fields['password2'].label = ''
        return form
    

#desactivados por problemas de redireccion
# class PasswordResetView(TemplateView):
#     template_name = 'registration/password_reset.html'

# class PasswordResetDoneView(TemplateView):
#     template_name = 'registration/password_reset_done.html'

# class PasswordResetConfirmView(TemplateView):
#     template_name = 'registration/password_reset_confirm.html'

# class PasswordResetCompleteView(TemplateView):
#     template_name = 'registration/password_reset_complete.html'


# def passwordReset(request):
#     return render(request, "registration/password_reset_form.html")