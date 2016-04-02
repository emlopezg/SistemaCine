# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proveedor', models.CharField(help_text='Introduce el nombre del proveedor', unique=True, max_length=20, verbose_name='Nombre del Proveedor', error_messages={'unique': 'Ya existe un proveedor con ese nombre,ingrese otro nombre'})),
                ('tel_fijo', models.CharField(help_text='Introduce un numero de telefono fijo del proveedor', max_length=10, verbose_name='Telefono fijo')),
                ('tel_celular', models.CharField(help_text='Introduce un numero de telefono celular del proveedor', max_length=10, verbose_name='Telefono celular')),
                ('direccion', models.CharField(help_text='Introduce direccion de la empresa o proveedor', max_length=50)),
            ],
        ),
    ]
