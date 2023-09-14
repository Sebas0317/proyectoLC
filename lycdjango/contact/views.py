from django.shortcuts import render,redirect
from .forms import Contactoformulario
from django.urls import reverse
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def contacto(request):
	contacto_form=Contactoformulario()
	if request.method == 'POST':
		contacto_form=Contactoformulario(data=request.POST)
		if contacto_form.is_valid():
			nombre = request.POST.get('nombre','')
			correo = request.POST.get('correo','')
			mensaje = request.POST.get('mensaje','')
			# envio de codigo
			correo = EmailMessage(
				"Comercializadora L&C: nuevo mensaje", 
			 	"De {} <{}>\n\nEscribio:\n\n{}".format(nombre, correo, mensaje),
				"smtp.gmail.com",
				["xmiguelx209@gmail.com"],
				reply_to= [correo]
			)
			try:
				correo.send()
				return redirect(reverse('contact')+"?ok")
			except:
				return redirect(reverse('contact')+"?fail")
	return render(request, 'contact/contacto.html',{'form':contacto_form})