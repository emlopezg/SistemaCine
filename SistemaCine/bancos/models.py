from django.db import models

# Create your models here.

class Banco(models.Model):
    nombre = models.CharField(max_length=20,)
    def __unicode__(self):
        return self.nombre


class CuentaCorriente(models.Model):
    codigocuenta = models.CharField(max_length=20,)
    saldo = models.IntegerField()
    banco = models.ForeignKey(Banco)
    def __unicode__(self):
        return self.codigocuenta
    class Meta:
        verbose_name = ("Cuenta Corriente")
        verbose_name_plural = ("Cuentas Corrientes")
    
class Chequera(models.Model):
    codigochequera = models.CharField(max_length=20,)
    rangoini = models.IntegerField()
    rangofin = models.IntegerField()    
    cuentacorriente = models.ForeignKey(CuentaCorriente)
    
    def __unicode__(self):
        return self.codigochequera
    
    class Meta:
        verbose_name = ("Chequera")
        verbose_name_plural = ("Chequeras")

class Cheque(models.Model):
    serie = models.CharField(max_length=20,)
    monto = models.IntegerField()
    chequera = models.ForeignKey(Chequera)
        
    def __unicode__(self):
        return self.serie