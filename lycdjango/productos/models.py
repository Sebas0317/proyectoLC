from django.db import models

# import uuid

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    cantidad_disponible = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    fecha_carga = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    tipo = models.ForeignKey(TipoProducto, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.nombre


class Especificacion(models.Model):
    producto = models.ForeignKey(Producto, related_name='especificaciones', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}: {self.valor}"
    
