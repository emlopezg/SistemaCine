# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
        ('bancos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('tipo', models.CharField(max_length=8, choices=[('MEN', 'Menores'), ('ADU', 'Adultos')])),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('cantidad_producto', models.IntegerField(default=0, verbose_name='Cantidad pedida')),
                ('medida', models.CharField(max_length=20, choices=[('LT', 'litros'), ('KL', 'kilos'), ('UN', 'unidades')])),
                ('total', models.IntegerField(help_text='Total a pagar al proveedor', null=True, blank=True)),
                ('aprobado', models.BooleanField(help_text='Si aprueba la orden de compra, se enviara la orden al proveedor')),
                ('cantidadrecibida', models.IntegerField(default=0, null=True, verbose_name='Cantidad de producto recibida', blank=True)),
                ('fecharecepcion', models.DateField(null=True, verbose_name='Fecha de Recepcion', blank=True)),
                ('fechaemision', models.DateField(null=True, verbose_name='Fecha de emision', blank=True)),
                ('factura', models.CharField(max_length=20, null=True, verbose_name='Numero de Factura', blank=True)),
                ('tipopago', models.CharField(blank=True, max_length=20, choices=[('CONTADO', 'Contado'), ('AMORTIZADO', 'Amortizado')])),
                ('diapago', models.IntegerField(blank=True, null=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28')])),
                ('meses', models.IntegerField(null=True, blank=True)),
                ('estado', models.BooleanField(help_text='Una vez que se reciban todos los productos se anula la orden de compra', verbose_name='Anulacion de orden de compra')),
                ('producto', models.ForeignKey(to='productos.Producto')),
                ('proveedor', models.ForeignKey(to='productos.Proveedor')),
            ],
            options={
                'verbose_name': 'Orden de Compra',
                'verbose_name_plural': 'Ordenes de compra',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=20, choices=[('PAGADO', 'Pagado'), ('PENDIENTE', 'Pendiente')])),
                ('total', models.IntegerField()),
                ('tipopago', models.CharField(max_length=20, choices=[('CONTADO', 'Contado'), ('AMORTIZADO', 'Amortizado')])),
                ('cheque', models.ForeignKey(blank=True, to='bancos.Cheque', null=True)),
                ('ordencompra', models.ForeignKey(to='stock.OrdenDeCompra')),
                ('proveedor', models.ForeignKey(to='productos.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numerofactura', models.CharField(max_length=20)),
                ('fecharecepcion', models.DateField()),
                ('fechaemision', models.DateField()),
                ('cantidadrecibida', models.IntegerField()),
                ('ordencompra', models.ForeignKey(to='stock.OrdenDeCompra')),
                ('producto', models.ForeignKey(to='productos.Producto')),
                ('proveedor', models.ForeignKey(to='productos.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=' ')),
                ('concepto', models.CharField(max_length=200)),
                ('ingreso', models.IntegerField()),
                ('egreso', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Ingreso y Egreso',
            },
        ),
        migrations.CreateModel(
            name='ReservaAsiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechareserva', models.DateField(verbose_name='Fecha de reserva')),
                ('cantidad_menor', models.IntegerField(default=0, help_text='Cantidad de asientos reservados para menores', verbose_name='Asientos(menores)')),
                ('cantidad_mayor', models.IntegerField(default=0, help_text='Cantidad de asientos reservados para adultos', verbose_name='Asientos (adultos)')),
                ('asientos', models.CharField(default='', max_length=20, verbose_name='Asientos reservados')),
                ('fechafuncion', models.DateField(verbose_name='Fecha de la funcion')),
                ('totalentrada', models.IntegerField(verbose_name='Total a pagar por las entradas')),
                ('totalcombo', models.IntegerField(verbose_name='Total a pagar por combo/s')),
                ('total', models.IntegerField(verbose_name='Total a pagar')),
                ('pagado', models.BooleanField(help_text='Cobrar al cliente una vez que venga a retirar la entrada')),
                ('combo', models.ForeignKey(to='productos.Combo')),
                ('horario', models.ForeignKey(to='cinema.Horario')),
                ('proyeccion', models.ForeignKey(to='cinema.Proyeccion')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
