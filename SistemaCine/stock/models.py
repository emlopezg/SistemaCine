from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from productos.models import Combo

# Create your models here.

class FacturaVenta(models.Model):
    codigo = models.CharField('Codigo de la factura', max_length=20)
    fecha = models.DateField()
    usuario = models.ForeignKey(User, null = True)

class FacturaVentaDetalle(models.Model):
    codigo_factura = models.ForeignKey(FacturaVenta, null = True)
    combo = models.ForeignKey(Combo, null = True)
    cantidad_combo = models.IntegerField()
    total = models.IntegerField()
    #entrada = models.ForeignKey()    aca vamos a facturar entradas juejue