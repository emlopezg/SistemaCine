from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from productos.models import Combo, Proveedor, Producto
from cinema.models import Proyeccion

# Create your models here.

class Venta(models.Model):
    #codigo = models.CharField('Codigo de la factura', max_length=20)
    fecha = models.DateField()
    usuario = models.ForeignKey(User, null = True)
    total = models.IntegerField()

class VentaDetalle(models.Model):
    codigo_factura = models.ForeignKey(Venta, null = True)
    entrada = models.ForeignKey(Proyeccion)
    cantidad = models.IntegerField()
    combo = models.ForeignKey(Combo, null = True)
    #cantidad_combo = models.IntegerField()
    #precio = models.OneToOneRel(Combo)

class OrdenDeCompra(models.Model):
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, null = True)
    total = models.IntegerField()
    
    def calcularTotal(self, producto, cantidad):
        producto = Producto.objects.filter(id=producto)
        total = cantidad * producto.precio_compra
        return total

class OrdenDeCompraDetalle(models.Model):
    orden = models.ForeignKey(OrdenDeCompra, null = True)
    producto = models.ForeignKey(Producto, null = True)
    cantidad = models.IntegerField()
