from django.shortcuts import render
from politicas.models import polprivacidad, acercade, terminos, polpago, polenvio, poldevoluiones

# Create your views here.
def privacidad(request):
    polprivas = polprivacidad.objects.all()
    return render(request, 'politicas/politica_privacidad.html',{'polprivas':polprivas})

def aboutme(request):
    sobrenosotros = acercade.objects.all()
    return render(request, 'politicas/sobre_nosotros.html',{'sobrenosotros':sobrenosotros})

def Terminos(request):
    TT = terminos.objects.all()
    return render(request, 'politicas/terminos.html',{'TT':TT})

def Politicapago(request):
    pagos = polpago.objects.all()
    return render(request, 'politicas/politica_pago.html',{'pagos':pagos})

def Politicaenvio(request):
    envios = polenvio.objects.all()
    return render(request, 'politicas/politica_envio.html',{'envios':envios})

def Politicadev(request):
    devoluciones = poldevoluiones.objects.all()
    return render(request, 'politicas/politica_devolucion.html',{'devoluciones':devoluciones})
