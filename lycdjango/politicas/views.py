from django.shortcuts import render
from politicas.models import Polprivacidad, Acercade, Terminos, Polpago, Polenvio, Poldevoluiones

def privacidad(request):
    polprivas = Polprivacidad.objects.all()
    context = {'polprivas': polprivas}
    return render(request, 'politicas/politica_privacidad.html', context)

def aboutme(request):
    sobrenosotros = Acercade.objects.all()
    context = {'sobrenosotros': sobrenosotros}
    return render(request, 'politicas/sobre_nosotros.html', context)

def terminos(request):
    terminos = Terminos.objects.all()
    context = {'terminos': terminos}
    return render(request, 'politicas/terminos.html', context)

def politica_pago(request):
    pagos = Polpago.objects.all()
    context = {'pagos': pagos}
    return render(request, 'politicas/politica_pago.html', context)

def politica_envio(request):
    envios = Polenvio.objects.all()
    context = {'envios': envios}
    return render(request, 'politicas/politica_envio.html', context)

def politica_devolucion(request):
    devoluciones = Poldevoluiones.objects.all()
    context = {'devoluciones': devoluciones}
    return render(request, 'politicas/politica_devolucion.html', context)
