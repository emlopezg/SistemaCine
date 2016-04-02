from django.shortcuts import render

# Create your views here.
'''
def refreshStock():
    from stock.models import Producto
    #if(Producto.objects.count()):
    no = Producto.objects.count()
    if no == None:
        return 3
        #else:
        #    return no + 1'''
from datetime import date

def generarFacturaCompra():
    date = date()
    #user = el usuario en ese momento
    