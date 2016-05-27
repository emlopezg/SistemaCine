# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.CharField(max_length=20)),
                ('monto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chequera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigochequera', models.CharField(max_length=20)),
                ('rangoini', models.IntegerField()),
                ('rangofin', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Chequera',
                'verbose_name_plural': 'Chequeras',
            },
        ),
        migrations.CreateModel(
            name='CuentaCorriente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigocuenta', models.CharField(max_length=20)),
                ('saldo', models.IntegerField()),
                ('banco', models.ForeignKey(to='bancos.Banco')),
            ],
            options={
                'verbose_name': 'Cuenta Corriente',
                'verbose_name_plural': 'Cuentas Corrientes',
            },
        ),
        migrations.AddField(
            model_name='chequera',
            name='cuentacorriente',
            field=models.ForeignKey(to='bancos.CuentaCorriente'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='chequera',
            field=models.ForeignKey(to='bancos.Chequera'),
        ),
    ]
