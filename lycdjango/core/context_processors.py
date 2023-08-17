from politicas.models import CorreoEmpresa  # Asegúrate de importar el modelo correcto

def correo_empresa(request):
    correo_empresa = CorreoEmpresa.objects.first()
    return {'correo_empresa': correo_empresa}
