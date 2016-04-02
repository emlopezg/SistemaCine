from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pelicula(models.Model):
    GENERO_CHOICES= (
    ("ACCION","Accion"),
    ("THRILLER","Thriller"),
    ("DOCUMENTAL","Documental"),
    ("ANIMACION","Animacion"),
    ("TERROR","Terror"),
    ("HORROR","Horror"),
    )
    nombre = models.CharField(max_length=100, help_text='Introduce el nombre de la pelicula', 
    unique = True, error_messages={'unique': ("Ya existe una pelicula con ese nombre,ingrese otro nombre"),
    })
    duracion = models.IntegerField(help_text='Introduce la duracion de la pelicula en minutos')
    director = models.CharField(max_length=30, help_text='Introduce el nombre del director de la pelicula')
    genero = models.CharField(max_length=15, choices = GENERO_CHOICES, default="ACCION")    
    descripcion = models.TextField(max_length=300, help_text='Sintaxis breve de la pelicula')
    imagen = models.FileField(upload_to= 'pelicula_pics', help_text = 'Sube una imagen ilustrativa de la pelicula')
    def __unicode__(self):
        return self.nombre
    
class Sala(models.Model):
    TIPO_CHOICES= (
    ("2D","Sala 2D"),
    ("3D","Sala 3D"),
    )
    codigo = models.CharField(max_length=10, unique = True, error_messages={
    'unique': ("Ya existe una sala con ese codigo,ingrese otro codigo"),
    })
    tipo = models.CharField(max_length=8, choices = TIPO_CHOICES, default="2D")
    filas = models.IntegerField()
    columnas = models.IntegerField()
    def __unicode__(self):
        return self.codigo

class Proyeccion(models.Model):
    codigo = models.CharField(max_length=10, unique = True, error_messages={
    'unique': ("Ya existe una proyeccion con ese codigo,ingrese otro codigo"),
    })
    pelicula = models.ForeignKey(Pelicula, on_delete = models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete = models.CASCADE)
    horario = models.TimeField()
    
    def __unicode__(self):
        return self.codigo