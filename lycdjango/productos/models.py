from django.db import models
from django.contrib.auth.models import User  #asociar comentarios a usuarios

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
    
#comentarios
class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  #asociar comentarios a usuarios
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario por {self.autor} en {self.producto.nombre}"
