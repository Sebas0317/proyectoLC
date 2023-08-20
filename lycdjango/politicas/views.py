from django.shortcuts import render
from politicas.models import polprivacidad

# Create your views here.
def privacidad(request):
    polprivas = polprivacidad.objects.all()
    return render(request, 'politicas/politica_privacidad.html',{'polprivas':polprivas})