from django.shortcuts import render
from politicas.models import Polprivacidad, Acercade, Terminos, Polpago, Polenvio, Poldevoluiones

# Create your views here.
def privacidad(request):
    polprivas = Polprivacidad.objects.all()
    return render(request, 'politicas/politica_privacidad.html',{'polprivas':polprivas})

def aboutme(request):
    sobrenosotros = Acercade.objects.all()
    return render(request, 'politicas/sobre_nosotros.html',{'sobrenosotros':sobrenosotros})

def Terminos(request):
    TT = Terminos.objects.all()
    return render(request, 'politicas/terminos.html',{'TT':TT})

def Politicapago(request):
    pagos = Polpago.objects.all()
    return render(request, 'politicas/politica_pago.html',{'pagos':pagos})

def Politicaenvio(request):
    envios = Polenvio.objects.all()
    return render(request, 'politicas/politica_envio.html',{'envios':envios})

def Politicadev(request):
    devoluciones = Poldevoluiones.objects.all()
    return render(request, 'politicas/politica_devolucion.html',{'devoluciones':devoluciones})
