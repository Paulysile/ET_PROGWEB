# Generated by Django 3.2.3 on 2021-06-25 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idServicio', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Servicio')),
                ('nombreServicio', models.CharField(max_length=50, verbose_name='Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('rut', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='RUT')),
                ('razonsocial', models.CharField(max_length=100, verbose_name='Razon Social')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.servicio')),
            ],
        ),
    ]