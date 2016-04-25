from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http.response import HttpResponseRedirect
from stock.forms import CompraForm
from datetime import date, datetime
from productos.models import Combo, ProductoFinal, Producto
from stock.models import OrdenDeCompra
# Create your views here.

def refreshStock(combo):
    '''A este metodo se le envia el id del combo, para que recupere el combo y
    descuente del stock la cantidad necesario por cada articulo
    -recuperar combo
    -recuperar productos finales
    -recuperar producto'''
    
    #combo = Combo.objects.get(id=combo) #se recupera el combo
    #lista de productos finales en combo
    for i in combo.productofinal.all():
        #productofinal = ProductoFinal.objects.get(id.)
        producto = Producto.objects.get(id =i.producto_id) #es producto id porque hace referencia a un number, no a un objetos
        if(producto.categoria == 'BEBIDA'):
            totalrestar = combo.cant_bebida*(i.volumen/float(1000))
            #print(productofinal,totalrestar)
        else:
            if(producto.categoria == "COMESTIBLE"):
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
    ordencompra.fecha = datetime.now()
    ordencompra.producto = p
    ordencompra.proveedor = p.proveedor
    ordencompra.aprobado = False
    ordencompra.estado = False
    ordencompra.save()
    
    #from stock.models import Producto
    #if(Producto.objects.count()):
    #no = Producto.objects.count()
    #if no == None:
        #return 3
        #else:
        #    return no + 1


    
def Comprar(request,):
    fecha = date.today()
    #user = co
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            combo = form.cleaned_data['combo']
            #pelicula = form.cleaned_data['pelicula']
            ''' venta = Venta.objects.create()
            venta.fecha = fecha
            venta.usuario = 'admin'
            #venta.ticket = 'proy'+fecha+
            venta.combo = combo.id
            venta.total = combo.precio
            venta.save()'''
            refreshStock(combo);
            return HttpResponseRedirect('/main')          
    else:
        data = {}
        form = CompraForm(data)
    return render_to_response("comprar.html", { 'form' : form  },context_instance=RequestContext(request))
    '''if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password= form.cleaned_data['password']
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']
            user= User.objects.create_user(username, email, password)
            user.first_name = nombre
            user.last_name = apellido
            user.save()
            return HttpResponseRedirect('/login')
    else:
        data = {}
        form= UserForm(data)
        
    return render_to_response("registrar.html", { 'form' : form  },context_instance=RequestContext(request))'''