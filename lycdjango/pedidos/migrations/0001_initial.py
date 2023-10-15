# Generated by Django 4.2 on 2023-10-12 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidosOrden',
            fields=[
                ('producto', models.CharField(max_length=100)),
                ('cantidad', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nombres', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=200)),
                ('numero_telefono', models.CharField(max_length=20)),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('estado_pedido', models.CharField(choices=[('Pendiente', 'Pendiente de envío'), ('EnProceso', 'En proceso'), ('Enviado', 'Enviado')], default='Pendiente', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
