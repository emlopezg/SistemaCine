from django.db import models

# Create your models here.

class Proveedor(models.Model):
    proveedor = models.CharField('Nombre del Proveedor',max_length=20, help_text='Introduce el nombre del proveedor', 
    unique = True, error_messages={'unique': ("Ya existe un proveedor con ese nombre,ingrese otro nombre"),
    })
    tel_fijo = models.CharField('Telefono fijo',max_length=10, help_text='Introduce un numero de telefono fijo del proveedor')
    tel_celular = models.CharField('Telefono celular',max_length=10, help_text='Introduce un numero de telefono celular del proveedor')
    direccion = models.CharField(max_length=50, help_text='Introduce direccion de la empresa o proveedor')
    def __unicode__(self):
        return self.proveedor.encode('utf8')
    
class Producto(models.Model):
    #mas adelante automatizar la generacion del codigo
    codigo = models.CharField('Codigo del Producto', max_length = 20,)
    producto = models.CharField('Descripcion del Producto', max_length=30,help_text='Introduce el nombre del producto',
    unique = True, error_messages ={'unique':'Ya existe ese producto, ingrese otro producto'})
    precio_compra = models.IntegerField('Precio compra', help_text='Introduce el precio de compra del producto')
    proveedor = models.ForeignKey(Proveedor, null =True, blank = True)
    stock = models.IntegerField('Stock', null = True, default = 0, help_text='Cantidad existente en kg/lt/un')
    
    def __unicode__(self):
        return self.producto
    '''class Meta:
        abstract = True
        ordering = ['producto']'''

class ProductoFinal(models.Model):
    codigo = models.CharField('Codigo del Producto', max_length = 20,)
    descripcion = models.CharField('Descripcion del Producto', max_length=30,help_text='Introduce el nombre del producto a la venta')
    producto = models.ManyToManyField(Producto)
    precio = models.IntegerField()

class Combo(models.Model):
    '''Abm de combos, para administrar los productos por combo'''
    codigo = models.CharField('Codigo del combo', max_length = 20)
    descripcion = models.TextField('Combo', max_length = 100, help_text='Introduce una descripcion del combo')
    producto = models.ManyToManyField(ProductoFinal)
    cant_bebida = models.IntegerField()
    cant_comestible = models.IntegerField()
    cant_golosina = models.IntegerField()
    precio = models.IntegerField()