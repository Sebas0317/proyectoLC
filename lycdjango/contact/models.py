from django.db import models

class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    asunto = models.CharField(max_length=100, default="Sin Asunto")  # Nuevo campo
    mensaje = models.TextField()

    ESTADOS = (
        ('respondido', 'Respondido'),
        ('visto', 'Visto'),
        ('no_respondido', 'No Respondido'),
    )
    estado = models.CharField(max_length=20, choices=ESTADOS, default='no_respondido')
    def __str__(self):
        return self.nombre

