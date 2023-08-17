from django.db import models

class GastosEnvio(models.Model):
    monto = models.PositiveIntegerField()

    def __str__(self):
        return f'Gastos de Envío: ${self.monto}'

class Cupon(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descuento = models.PositiveIntegerField()

    def __str__(self):
        return self.codigo
    
class CorreoEmpresa(models.Model):
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.correo