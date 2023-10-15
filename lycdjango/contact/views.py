from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import MensajeForm
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect



def contacto(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()  # Esto guardará el mensaje en la base de datos
             # Redirige a una página de éxito

    form = MensajeForm()  # Crea una instancia del formulario en caso de que el método sea GET
    messages.success(request, 'El producto se ha añadido al carrito correctamente.')
    return render(request, 'contact/contacto.html', {'form': form})
