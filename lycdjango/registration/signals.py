from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_usuarios_group(sender, instance, created, **kwargs):
    if created:
        try:
            usuario = Group.objects.get(name='usuario')
        except Group.DoesNotExist:
            usuario = Group.objects.create(name='usuario')
            
            
        instance.user.groups.add(usuario)