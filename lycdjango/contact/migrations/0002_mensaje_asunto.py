# Generated by Django 4.2 on 2023-10-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='asunto',
            field=models.CharField(default='Sin Asunto', max_length=100),
        ),
    ]
