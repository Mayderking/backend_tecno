# Generated by Django 5.1.4 on 2024-12-20 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]
