from politicas.models import CorreoEmpresa, Copyright  # Asegúrate de importar el modelo correcto

def correo_empresa(request):
    correo_empresa = CorreoEmpresa.objects.first()
    return {'correo_empresa': correo_empresa}

def copy_right(request):
    copy = Copyright.objects.first()
    return {'copy': copy}