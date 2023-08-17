from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#perfil usuario
class perfilUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil', verbose_name='Usuario')


    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username
    
def crear_perfilUser(sender, instance, created, **kwargs):
    if created:
        perfilUser.objects.create(user=instance)

def guardar_perdilUser(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(crear_perfilUser, sender=User)
post_save.conect(guardar_perdilUser, sender=User)
