from politicas.models import CorreoEmpresa, copyright  # Asegúrate de importar el modelo correcto

def correo_empresa(request):
    correo_empresa = CorreoEmpresa.objects.first()
    return {'correo_empresa': correo_empresa}

def copy_right(request):
    copy = copyright.objects.first()
    return {'copy': copy}