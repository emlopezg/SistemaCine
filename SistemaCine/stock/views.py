from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http.response import HttpResponseRedirect
from stock.forms import CompraForm
from datetime import date, datetime
from productos.models import Combo, ProductoFinal, Producto
from stock.models import OrdenDeCompra
from cinema.models import Proyeccion, Pelicula, Sala
from stock.models import ReservaAsiento, Asiento
from django.contrib.auth.models import User
# Create your views here.
PRECIO_ADULTOS_3D = 40000
PRECIO_ADULTOS_2D = 30000
PRECIO_NINHOS_3D = 30000
PRECIO_NINHOS_2D = 20000 
   
    #from stock.models import Producto
    #if(Producto.objects.count()):
    #no = Producto.objects.count()
    #if no == None:
        #return 3
        #else:
        #    return no + 1
 
def Reserva(request,):
    print("Llego hasta aca")
    if request.method == 'POST':
        print ("llego hasta reques.method post")
        form = CompraForm(request.POST)
        if form.is_valid():
            print ("llego hasta form.is valid")
            combo = form.cleaned_data['combo']
            pelicula = form.cleaned_data['pelicula']
            cantidadmenores = form.cleaned_data['cantidadmenores']
            cantidadmayores = form.cleaned_data['cantidadmayores']
            hora = form.cleaned_data['hora']
            fecha = form.cleaned_data['fecha']
            asientos = form.cleaned_data['asientos_reservados']
                  
            reserva = ReservaAsiento()
            reserva.fechareserva = date.today()
            reserva.usuario = User.objects.get(username = request.user.username)
            reserva.horario = hora
            reserva.proyeccion = Proyeccion.objects.get(pelicula = Pelicula.objects.get(nombre = pelicula))
            reserva.fechafuncion = fecha
            reserva.cantidad_menor = cantidadmenores;
            reserva.cantidad_mayor = cantidadmayores;
            sala = Sala.objects.get(id = reserva.proyeccion.sala.id)
            if (sala.tipo == '3D'):
                reserva.totalentrada = (cantidadmayores*PRECIO_ADULTOS_3D) + (cantidadmenores*PRECIO_NINHOS_3D)
            else:
                reserva.totalentrada = (cantidadmayores*PRECIO_ADULTOS_2D) + (cantidadmenores*PRECIO_NINHOS_2D)
            reserva.asientos = asientos;
            reserva.combo = combo
            reserva.totalcombo = combo.precio
            reserva.total = reserva.totalcombo + reserva.totalentrada
            reserva.pagado = False
            reserva.save()
            #reserva.combo.add(combo)
            
            return HttpResponseRedirect('/main')          
    else:
        data = {}
        form = CompraForm(data)
    return render_to_response("compra.html", { 'form' : form  },context_instance=RequestContext(request))
