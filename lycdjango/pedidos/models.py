from django.db import models
from django.contrib.auth.models import User


class PedidosOrden(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    nombres = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    numero_telefono = models.CharField(max_length=20)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    ESTADOS_PEDIDO = [
        ('Pendiente', 'Pendiente de envío'),
        ('EnProceso', 'En proceso'),
        ('Enviado', 'Enviado'),
    ]
    estado_pedido = models.CharField(
    max_length=10,
    choices=ESTADOS_PEDIDO,
    default='Pendiente',
    )
    
    def __str__(self):
        return f"Pedido #{self.id_pedido}"


class PedidosByUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pedidos = models.ManyToManyField(PedidosOrden, related_name='usuarios')

    def __str__(self):
     return f'Usuario: {self.user.username}, Pedidos: {", ".join([str(p) for p in self.pedidos.all()])}'

   

