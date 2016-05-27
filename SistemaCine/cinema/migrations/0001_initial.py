# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(help_text='Introduce el nombre de la pelicula', unique=True, max_length=100, error_messages={'unique': 'Ya existe una pelicula con ese nombre,ingrese otro nombre'})),
                ('duracion', models.IntegerField(help_text='Introduce la duracion de la pelicula en minutos')),
                ('director', models.CharField(help_text='Introduce el nombre del director de la pelicula', max_length=30)),
                ('genero', models.CharField(default='ACCION', max_length=15, choices=[('ACCION', 'Accion'), ('THRILLER', 'Thriller'), ('DOCUMENTAL', 'Documental'), ('ANIMACION', 'Animacion'), ('TERROR', 'Terror'), ('HORROR', 'Horror')])),
                ('descripcion', models.TextField(help_text='Sintaxis breve de la pelicula', max_length=300)),
                ('imagen', models.FileField(help_text='Sube una imagen ilustrativa de la pelicula', upload_to='pelicula_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Proyeccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desde', models.DateField()),
                ('hasta', models.DateField()),
                ('pelicula', models.ForeignKey(to='cinema.Pelicula')),
            ],
            options={
                'verbose_name': 'Proyeccion',
                'verbose_name_plural': 'Proyecciones',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=10, error_messages={'unique': 'Ya existe una sala con ese codigo,ingrese otro codigo'})),
                ('tipo', models.CharField(default='2D', max_length=8, choices=[('2D', 'Sala 2D'), ('3D', 'Sala 3D')])),
                ('filas', models.IntegerField()),
                ('columnas', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='proyeccion',
            name='sala',
            field=models.ForeignKey(to='cinema.Sala'),
        ),
    ]
