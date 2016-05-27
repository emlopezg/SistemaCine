# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20, verbose_name=b'Codigo del combo')),
                ('descripcion', models.TextField(help_text=b'Introduce una descripcion del combo', max_length=100, verbose_name=b'Combo')),
                ('imagen', models.FileField(help_text=b'Sube una imagen ilustrativa de la pelicula', upload_to=b'pelicula_pics')),
                ('cant_bebida', models.IntegerField()),
                ('cant_comestible', models.IntegerField()),
                ('cant_golosina', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(default=b'Prod', help_text=b'Introduce el codigo del producto', max_length=20, verbose_name=b'Codigo del Producto', error_messages={b'unique': b'Ya existe un producto con ese codigo,ingrese otro codigo'})),
                ('producto', models.CharField(help_text=b'Introduce descripcion del producto -> descripcion-tamanho', unique=True, max_length=50, verbose_name=b'Descripcion del Producto', error_messages={b'unique': b'Ya existe ese producto, ingrese otro producto'})),
                ('categoria', models.CharField(default=b'BEBIDA', max_length=20, choices=[(b'BEBIDA', b'Bebida'), (b'COMESTIBLE', b'Comestible'), (b'INSBEBIDA', b'Insumo p/Bebida'), (b'INSCOMESTIBLE', b'Insumo p/Comestible'), (b'GOLOSINAS', b'Golosinas')])),
                ('precio_compra', models.IntegerField(help_text=b'Introduce el precio de compra por unidad', verbose_name=b'Precio compra')),
                ('stock', models.FloatField(default=0, help_text=b'Cantidad existente en kl/lt/un', null=True, verbose_name=b'Stock')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoFinal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20, verbose_name=b'Codigo del Producto')),
                ('descripcion', models.CharField(help_text=b'Introduce el nombre del producto a la venta', max_length=30, verbose_name=b'Descripcion del Producto')),
                ('volumen', models.IntegerField(help_text=b'Introduce el volumen a vender por unidad en gr/cc')),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
                'verbose_name': 'Producto Final',
                'verbose_name_plural': 'Productos Finales',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proveedor', models.CharField(help_text=b'Introduce el nombre del proveedor', unique=True, max_length=20, verbose_name=b'Nombre del Proveedor', error_messages={b'unique': b'Ya existe un proveedor con ese nombre,ingrese otro nombre'})),
                ('tel_fijo', models.CharField(help_text=b'Introduce un numero de telefono fijo del proveedor', max_length=10, verbose_name=b'Telefono fijo')),
                ('tel_celular', models.CharField(help_text=b'Introduce un numero de telefono celular del proveedor', max_length=10, verbose_name=b'Telefono celular')),
                ('direccion', models.CharField(help_text=b'Introduce direccion de la empresa o proveedor', max_length=50)),
                ('correo', models.EmailField(help_text=b'Introduce la direccion de correo del proveedor', max_length=50)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(to='productos.Proveedor', null=True),
        ),
        migrations.AddField(
            model_name='combo',
            name='producto',
            field=models.ManyToManyField(to='productos.Producto'),
        ),
        migrations.AddField(
            model_name='combo',
            name='productofinal',
            field=models.ManyToManyField(to='productos.ProductoFinal'),
        ),
    ]
