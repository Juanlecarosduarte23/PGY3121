# Generated by Django 4.2.2 on 2023-07-13 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_boleta_contacto_alter_producto_nombre_detalle_boleta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
    ]
