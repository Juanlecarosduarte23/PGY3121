from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(blank=True, max_length=50, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('nombre', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='nombre')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('precio', models.CharField(max_length=50, verbose_name='Precio')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria', verbose_name='Categoria')),
            ],
        ),
    ]






