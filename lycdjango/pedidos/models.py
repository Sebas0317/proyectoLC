# models.py en la aplicación pedidos
from django.db import models
from productos.models import Producto  # Importa el modelo Producto

class Pedido(models.Model):
    nombres = models.CharField(max_length=255)
    correo = models.EmailField()
    direccion = models.CharField(max_length=255)
    numero_telefono = models.CharField(max_length=15)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con Producto
    cantidad = models.PositiveIntegerField()
    total_compra = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido de {self.nombres}'

    # Agrega cualquier otra información que desees para tus pedidos
