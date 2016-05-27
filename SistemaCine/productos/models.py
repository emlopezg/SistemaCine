from django.db import models
from django.db.models.aggregates import Count

# Create your models here.

class Proveedor(models.Model):
    '''Clase para registrar datos del proveedor'''
    
    proveedor = models.CharField('Nombre del Proveedor',max_length=20, help_text='Introduce el nombre del proveedor', 
            unique = True, error_messages={'unique': ("Ya existe un proveedor con ese nombre,ingrese otro nombre"),})
    tel_fijo = models.CharField('Telefono fijo',max_length=10, 
            help_text='Introduce un numero de telefono fijo del proveedor')
    tel_celular = models.CharField('Telefono celular',max_length=10, 
            help_text='Introduce un numero de telefono celular del proveedor')
    direccion = models.CharField(max_length=50, help_text='Introduce direccion de la empresa o proveedor')
    correo = models.EmailField(max_length = 50, help_text= 'Introduce la direccion de correo del proveedor')
    
    def __unicode__(self):
        return self.proveedor.encode('utf8')
    
    class Meta:
        verbose_name = ("Proveedor")
        verbose_name_plural = ("Proveedores")

class Producto(models.Model):
    '''Clase para registrar datos de productos. Algunos productos son materia prima
    para producir otro producto final'''
    
    CATEGORIA_CHOICES= (
    ("BEBIDA","Bebida"),
    ("COMESTIBLE","Comestible"),
    ("INSBEBIDA","Insumo p/Bebida"),
    ("INSCOMESTIBLE","Insumo p/Comestible"),
    ("GOLOSINAS","Golosinas"),
    )
    codigo = models.CharField('Codigo del Producto', max_length = 20, 
            default = 'Prod', help_text='Introduce el codigo del producto', 
            error_messages={'unique': ("Ya existe un producto con ese codigo,ingrese otro codigo"),})
    producto = models.CharField('Descripcion del Producto', max_length=50,
            help_text='Introduce descripcion del producto -> descripcion-tamanho',
    unique = True, error_messages ={'unique':'Ya existe ese producto, ingrese otro producto'})
    categoria = models.CharField(max_length =20,choices = CATEGORIA_CHOICES, default="BEBIDA")
    precio_compra = models.IntegerField('Precio compra', help_text='Introduce el precio de compra por unidad')
    proveedor = models.ForeignKey(Proveedor, null=True, )
    stock = models.FloatField('Stock', null = True, default = 0, help_text='Cantidad existente en kl/lt/un')
    
    def __unicode__(self):
        return self.producto
    
    ''' def generarCodigo(self,clase):
        objeto = Count(clase.objects.all())
        id = objeto+1
        if objeto:
            codigo = clase+id
            return codigo'''

class ProductoFinal(models.Model):
    '''Clase para registrar datos de Productos finales. Estos productos se hacen a base
    de otro producto.'''
    
    codigo = models.CharField('Codigo del Producto', max_length = 20,)
    descripcion = models.CharField('Descripcion del Producto', max_length=30,
                help_text='Introduce el nombre del producto a la venta')
    producto = models.ForeignKey(Producto)
    volumen = models.IntegerField(help_text='Introduce el volumen a vender por unidad en gr/cc')
    
    def __unicode__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = ("Producto Final")
        verbose_name_plural = ("Productos Finales")
        #ordering = ("user", "name")
        #unique_together = ("user", "name")


class Combo(models.Model):
    '''Clase para registrar datos de Combo. Los datos incluyen: productos utilizados, productos finales,
    insumos y cantidad utilizados en cada combo'''
    
    codigo = models.CharField('Codigo del combo', max_length = 20)
    descripcion = models.TextField('Combo', max_length = 100, help_text='Introduce una descripcion del combo')
    productofinal = models.ManyToManyField(ProductoFinal)
    producto = models.ManyToManyField(Producto,)
    imagen = models.FileField(upload_to= 'pelicula_pics', help_text = 'Sube una imagen ilustrativa de la pelicula')
    cant_bebida = models.IntegerField()
    cant_comestible = models.IntegerField()
    cant_golosina = models.IntegerField()
    precio = models.IntegerField()
    
    def get_fields_and_values(self):
            return [(field, field.value_to_string(self)) for field in Combo._meta.fields]
    
    def __unicode__(self):
        return self.codigo