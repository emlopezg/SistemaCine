from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from productos.models import Combo, Proveedor, Producto
from cinema.models import Proyeccion, Horario, Pelicula
from django.core.mail.message import EmailMessage
from bancos.models import Cheque
from datetime import date

# Create your models here.

class OrdenDeCompra(models.Model):
    MEDIDA_CHOICES= (
    ("LT","litros"),
    ("KL","kilos"),
    ("UN","unidades"),
    )
    TIPOPAGO_CHOICES= (
    ('CONTADO','Contado'),
    ('AMORTIZADO','Amortizado'),
    )
    DIA_CHOICES= (
    ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), 
    ('8','8'), ('9','9'), ('10','10'), ('11','11'), ('12','12'), ('13','13'), 
    ('14','14'), ('15','15'), ('16','16'), ('17','17'), ('18','18'), ('19','19'), 
    ('20','20'), ('21','21'), ('22','22'), ('23','23'), ('24','24'),('25','25'),
    ('26','26'), ('27','27'), ('28','28'),
    )
    
    fecha = models.DateField()
    producto = models.ForeignKey(Producto,)
    proveedor = models.ForeignKey(Proveedor,)
    cantidad_producto = models.IntegerField('Cantidad pedida',default = 0)
    medida = models.CharField(max_length =20,choices = MEDIDA_CHOICES,)
    total = models.IntegerField(help_text='Total a pagar al proveedor', null = True, blank = True)
    aprobado = models.BooleanField(help_text="Si aprueba la orden de compra, se enviara la orden al proveedor")
    cantidadrecibida = models.IntegerField('Cantidad de producto recibida', default = 0, null = True, blank = True)
    fecharecepcion = models.DateField('Fecha de Recepcion', null = True, blank = True)
    fechaemision = models.DateField('Fecha de emision',null = True, blank = True)
    factura = models.CharField('Numero de Factura',max_length =20, null = True, blank = True)
    tipopago = models.CharField(max_length =20,choices = TIPOPAGO_CHOICES, blank = True)
    diapago = models.IntegerField(choices = DIA_CHOICES, null = True, blank = True)
    meses = models.IntegerField(null = True, blank = True)
    #en save verificar que el total recibido. Si es igual al total pedido, marcar como anulada la orden    
    estado = models.BooleanField('Anulacion de orden de compra', help_text="Una vez que se reciban todos los productos se anula la orden de compra")
    class Meta:
        verbose_name = ("Orden de Compra")
        verbose_name_plural = ("Ordenes de compra")
        
    def __unicode__(self):
        return self.producto.producto
    
    
    def save(self, *args, **kwargs):
        if(self.cantidad_producto != 0):
            producto = Producto.objects.get(id=self.producto.id)
            totalproducto = self.cantidad_producto*producto.precio_compra
            self.total = totalproducto
        
        if(self.cantidadrecibida):
            print 'Fueron recibidos los productos, se aumenta el stock. Se guarda un informe de recepcion'
            producto = Producto.objects.get(id=self.producto.id)
            producto.stock = producto.stock + self.cantidadrecibida
            producto.save()
            nuevarecepcion = Recepcion()
            nuevarecepcion.ordencompra = OrdenDeCompra.objects.get(id = self.id)
            nuevarecepcion.proveedor = self.proveedor
            nuevarecepcion.numerofactura = self.factura
            nuevarecepcion.fecharecepcion = self.fecharecepcion
            nuevarecepcion.fechaemision = self.fechaemision
            nuevarecepcion.producto = self.producto
            nuevarecepcion.cantidadrecibida = self.cantidadrecibida
            nuevarecepcion.save()
            
            nuevopago = Pago()
            nuevopago.ordencompra = OrdenDeCompra.objects.get(id = self.id)
            nuevopago.proveedor = self.proveedor
            nuevopago.estado = 'PENDIENTE'
            nuevopago.total = self.cantidadrecibida * self.producto.precio_compra
            nuevopago.tipopago = self.tipopago
            nuevopago.save()

        ordenes = Recepcion.objects.filter(ordencompra = self.id)
        #si hay recepciones que hacen referencia a la orden de compra, se seleccionan y si alcanzan
        #la cantidad de productos pedidos, se anula la orden de compra 
        if(ordenes):
            totalrecepcionorden = 0
            for i in ordenes:
                totalrecepcionorden = totalrecepcionorden + i.cantidadrecibida
                
            if(totalrecepcionorden>=self.cantidad_producto):
                self.estado = True
        
        super(OrdenDeCompra, self).save(*args, **kwargs) # Call the "real" save() method.        
        
        if(self.aprobado is True):
            print 'Fue aprobada la orden'
            #emailusuario = User
            encabezado= 'Orden de compra VMT '
            proveedor = Proveedor.objects.get(id = self.proveedor.id)
            producto = Producto.objects.get(id = self.producto.id)
            emailusuario = Proveedor.objects.get(id = self.proveedor.id)
            cuerpo= 'Buenos dias, Se solicita al proveedor '+str(proveedor.proveedor)
            #pdf = generar_pdf(OrdenDeCompra)
            #cuerpo = cuerpo.encode('ascii','ignore')
            correo = EmailMessage(subject=encabezado, body=cuerpo, to=[emailusuario.correo])
            #correo.attach_file('/images/weather_map.png') #para anhadir adjunto
            #correo.send()

class Recepcion(models.Model):
    proveedor = models.ForeignKey(Proveedor)
    ordencompra = models.ForeignKey(OrdenDeCompra)
    numerofactura = models.CharField(max_length=20,)
    fecharecepcion = models.DateField()
    fechaemision = models.DateField()
    producto = models.ForeignKey(Producto)
    cantidadrecibida = models.IntegerField()
    
    def __unicode__(self):
        return self.proveedor.proveedor

class Pago(models.Model):
    ESTADO_CHOICES= (
    ('PAGADO','Pagado'),
    ('PENDIENTE','Pendiente'),
    )
    
    PAGO_CHOICES = (
    ('CONTADO','Contado'),
    ('AMORTIZADO','Amortizado'),
    )
    
    cheque = models.ForeignKey(Cheque, null = True, blank= True)
    ordencompra = models.ForeignKey(OrdenDeCompra)
    proveedor = models.ForeignKey(Proveedor)
    estado = models.CharField(max_length=20,choices = ESTADO_CHOICES)
    total = models.IntegerField()
    tipopago = models.CharField(max_length=20,choices = PAGO_CHOICES)
    
    def __unicode__(self):
        return self.proveedor.proveedor

class Registro(models.Model):
    ESTADO_CHOICES= (
    ('INGRESO','Ingreso'),
    ('EGRESO','EGRESO'),
    )
    #PARA CADA TRANSACCION VOY A IR GUARDANDO, PERO VOY A AGREGAR UNA LINEA FINAL DONDE VOY A PONER EL TOTAL
    #VOY A CREAR UNA PRIMERA LINEA QUE SEA TOTAL JAJAJA XD y cada vez que haya una transaccion voy a sumar o restar :3 wii
    fecha = models.DateField(default = ' ')
    concepto = models.CharField(max_length = 200, )
    ingreso = models.IntegerField()
    egreso = models.IntegerField()
    
    def __unicode__(self):
        return self.concepto
    
    class Meta:
        verbose_name = ("Registro")
        verbose_name_plural = ("Ingreso y Egreso")

class Asiento(models.Model):
    TIPO_CHOICES= (
    ("MEN","Menores"),
    ("ADU","Adultos"),
    )
    numero = models.IntegerField()
    tipo = models.CharField(max_length=8, choices = TIPO_CHOICES,)
    cantidad = models.IntegerField()

class ReservaAsiento(models.Model):
    fechareserva = models.DateField('Fecha de reserva')
    usuario = models.ForeignKey(User)
    proyeccion = models.ForeignKey(Proyeccion)
    horario = models.ForeignKey(Horario)
    cantidad_menor = models.IntegerField('Asientos(menores)', default=0, help_text= 'Cantidad de asientos reservados para menores')
    cantidad_mayor = models.IntegerField('Asientos (adultos)', default=0, help_text= 'Cantidad de asientos reservados para adultos')
    asientos = models.CharField('Asientos reservados', max_length=20, default="")
    fechafuncion = models.DateField('Fecha de la funcion')
    totalentrada = models.IntegerField('Total a pagar por las entradas')
    combo = models.ForeignKey(Combo)
    totalcombo = models.IntegerField('Total a pagar por combo/s')
    total = models.IntegerField('Total a pagar')
    pagado = models.BooleanField(help_text = 'Cobrar al cliente una vez que venga a retirar la entrada')
    
    def __unicode__(self):
        return str(self.fechareserva)
    
    def save(self, *args, **kwargs):
        #al confirmar el pago se debe descontar de stock
        #en teoria deberia tambien imprimir el ticket
        if(self.pagado is True):
            refreshStock(self.combo)
            ingentrada = Registro()
            ingentrada.fecha = date.today()
            ingentrada.concepto = 'Venta de tickets de cine. Pelicula '+str(self.proyeccion.pelicula)+'. Cantidad '+str(self.cantidad_menor+self.cantidad_mayor)+'.'
            ingentrada.ingreso = self.totalentrada
            ingentrada.egreso = 0
            ingentrada.save()
            totalbalance = Registro.objects.get(id = 1)
            totalbalance.ingreso = totalbalance.ingreso + ingentrada.ingreso
            totalbalance.save()
            if (self.combo):
                combo = Combo.objects.get(id = self.combo.id)
                ingcombo = Registro()
                ingcombo.fecha = date.today()
                ingcombo.concepto = 'Venta de Combo '+combo.descripcion+'.'
                ingcombo.ingreso = self.totalcombo
                ingcombo.egreso = 0
                ingcombo.save()
                totalbalance = Registro.objects.get(id = 1)
                totalbalance.ingreso = totalbalance.ingreso + ingcombo.ingreso
                totalbalance.save()
        super(ReservaAsiento, self).save(*args, **kwargs) #Call the "real" save() method.


def refreshStock(combo):
    '''A este metodo se le envia el id del combo, para que recupere el combo y
    descuente del stock la cantidad necesario por cada articulo
    -recuperar combo
    -recuperar productos finales
    -recuperar producto''' 
    print('llega hasta refresh')
    print(combo.productofinal)
    #combo = Combo.objects.get(id=combo) #se recupera el combo
    #lista de productos finales en combo
    for i in combo.productofinal.all():
        #productofinal = ProductoFinal.objects.get(id.)
        print('llega hasta el for de producto final')
        producto = Producto.objects.get(id =i.producto_id) #es producto id porque hace referencia a un number, no a un objetos
        if(producto.categoria == 'BEBIDA'):
            print('llega hasta la resta de bebida')
            totalrestar = combo.cant_bebida*(i.volumen/float(1000))
            #print(productofinal,totalrestar)
        else:
            if(producto.categoria == "COMESTIBLE"):
                print('llega hasta la resta de comestible')
                totalrestar = combo.cant_comestible*(i.volumen/float(1000))
                #print(productofinal,totalrestar)
                if(i.descripcion.find('pororo')):
                    pfs = Producto.objects.get(codigo = 'Prod3')
                    pfs.stock = pfs.stock - (20/float(1000))
                    pfs.save()
                    controlarStock(pfs.id)
                    pfa = Producto.objects.get(codigo = 'Prod4')
                    pfa.stock = pfa.stock - (100/float(1000))
                    pfa.save()
                    controlarStock(pfa.id)
        producto.stock = producto.stock - totalrestar
        producto.save()
        controlarStock(producto.id)  
    #lista de productos de un combo
    for i in combo.producto.all():
        producto = Producto.objects.get(id = i.id)
        if (producto.categoria == 'INSBEBIDA'):
            producto.stock = producto.stock - combo.cant_bebida
        else:
            if (producto.categoria == 'INSCOMESTIBLE'):
                producto.stock = producto.stock - combo.cant_comestible
            else:
                producto.stock = producto.stock - combo.cant_golosina
        
        producto.save()
        controlarStock(producto.id)

def controlarStock(producto):
    p = Producto.objects.get(id = producto)
    if (p.stock <= 10):
        generarOrdenDeCompra(p.id)

def generarOrdenDeCompra(producto):
    p = Producto.objects.get(id = producto)
    ordencompra = OrdenDeCompra()
    ordencompra.fecha = date.today()
    ordencompra.producto = p
    ordencompra.proveedor = p.proveedor
    ordencompra.aprobado = False
    ordencompra.estado = False
    ordencompra.save()
