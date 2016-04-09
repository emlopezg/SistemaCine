from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http.response import HttpResponseRedirect
from stock.forms import CompraForm
from datetime import date
# Create your views here.

def refreshStock(combo):
    '''A este metodo se le envia el id del combo, para que recupere el combo y
    descuente del stock la cantidad necesario por cada articulo'''
    pass
    #from stock.models import Producto
    #if(Producto.objects.count()):
    #no = Producto.objects.count()
    #if no == None:
        #return 3
        #else:
        #    return no + 1

def Comprar(request):
    date = date()
    #user = el usuario en ese momento
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            combo = form.cleaned_data['combo']
            refreshStock(combo);
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