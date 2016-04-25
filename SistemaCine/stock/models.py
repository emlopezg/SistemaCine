from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from productos.models import Combo, Proveedor, Producto
from cinema.models import Proyeccion
from django.core.mail.message import EmailMessage
from datetime import date, datetime

from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from io import BytesIO

# Create your models here.

class Venta(models.Model):
    #codigo = models.CharField('Codigo de la factura', max_length=20)
    fecha = models.DateField()
    usuario = models.ForeignKey(User, null = True)
    #ticket = models.CharField(max_length=30, )#este codigo se va a generar con fecha-proyeccion-tipo
    combo = models.ForeignKey(Combo, null = True)
    total = models.IntegerField()

'''class VentaDetalle(models.Model):
    ticket = models.ForeignKey(Venta, null = True)
    combo = models.ForeignKey(Combo, null = True)
    #cantidad_combo = models.IntegerField()
    #precio = models.OneToOneRel(Combo)'''

class OrdenDeCompra(models.Model):
    fecha = models.DateField()
    producto = models.ForeignKey(Producto, null = True)
    proveedor = models.ForeignKey(Proveedor, null = True)
    cantidad_producto = models.IntegerField(default = 0)
    total = models.IntegerField(default = 0)
    aprobado = models.BooleanField(help_text="Si aprueba la orden de compra, se enviara la orden al proveedor")
    estado = models.BooleanField('Recibido', help_text="Marque una vez que se hayan recibido los productos")
    
    def __unicode__(self):
        return self.producto.producto
    
    def save(self, *args, **kwargs):
        if(self.cantidad_producto != 0):
            producto = Producto.objects.get(id=self.producto.id)
            totalproducto = self.cantidad_producto*producto.precio_compra
            self.total = totalproducto
        if(self.estado is True):
            print 'Fueron recibidos los productos, se aumenta el stock'
            producto = producto = Producto.objects.get(id=self.producto.id)
            producto.stock = producto.stock + self.cantidad_producto
            producto.save()
        
        super(OrdenDeCompra, self).save(*args, **kwargs) # Call the "real" save() method.
        
        if(self.aprobado is True):
            print 'Fue aprobada la orden'
            #emailusuario = User
            encabezado= 'Orden de compra VMT '
            proveedor = Proveedor.objects.get(id = self.proveedor.id)
            producto = Producto.objects.get(id = self.producto.id)
            emailusuario = Proveedor.objects.get(id = self.proveedor.id)  #se recupera el nombre de usuario a quien esta asignado el UH
            cuerpo="Se solicita al producto " + producto.producto
            #pdf = generar_pdf(OrdenDeCompra)
            correo = EmailMessage(subject=encabezado, body=[cuerpo], to=[emailusuario.correo])
            correo.send()      

def generar_pdf(orden):
    print "Genero el PDF"
    #response = HttpResponse(content_type='application/pdf')
    pdf_name = "ordencompra.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    #response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    ordencompra = []
    styles = getSampleStyleSheet()
    header = Paragraph("Orden de compra", styles['Heading1'])
    ordencompra.append(header)
    headings = ('Fecha', 'Producto', 'Proveedor', 'Cantidad Pedida')
    datos = [(orden)] #for p in OrdenCompra.objects.all()]
    print datos

    '''t = Table([headings] + datos)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))'''
    ordencompra.append(datos)
    #doc.build(ordencompra)
    #response.write(buff.getvalue())
    #buff.close()
    #return response
    return ordencompra


class ControlStock(models.Model):
    
           
    '''def calcularTotal(self):
        producto = Producto.objects.filter(id=self.producto)
        total = self.cantidad_producto*producto.precio_compra
        self.total = total'''
    
'''    
class OrdenDeCompraDetalle(models.Model):
    orden = models.ForeignKey(OrdenDeCompra, null = True)
    producto = models.ForeignKey(Producto, null = True)
    cantidad = models.IntegerField()
'''
