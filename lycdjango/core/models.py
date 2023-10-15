from django.db import models

class Comentario(models.Model):
    nombre_comprador = models.CharField(max_length=100)
    comentario = models.TextField()
    imagen = models.ImageField(upload_to='comentarios/', help_text='La imagen debe tener al menos 200x200 píxeles.')

    def __str__(self):
        return self.nombre_comprador
