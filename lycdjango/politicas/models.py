from django.db import models
from ckeditor.fields import RichTextField
from decimal import Decimal

class GastosEnvio(models.Model):
    monto = models.PositiveIntegerField()

    def __str__(self):
        return f'Gastos de Envío: ${self.monto}'

class Cupon(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.codigo
    
class CorreoEmpresa(models.Model):
    direccion = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.correo
    
class BrandImage(models.Model):
    image = models.ImageField(upload_to='brand_images/')

class Polprivacidad(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = RichTextField()

    def __str__(self):
        return self.titulo
    
class Acercade(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = RichTextField()

    def __str__(self):
        return self.titulo
    

class Terminos(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = RichTextField()

    def __str__(self):
        return self.titulo

class Polpago(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = RichTextField()

    def __str__(self):
        return self.titulo
    
class Polenvio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = RichTextField()

    def __str__(self):
        return self.titulo
    
class Poldevoluiones(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = RichTextField()

    def __str__(self):
        return self.titulo
    
class Copyright(models.Model):
    frase = models.CharField(max_length=255)

    def __str__(self):
        return self.frase