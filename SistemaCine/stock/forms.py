from django import forms
from cinema.models import Proyeccion
from productos.models import Combo

class CompraForm(forms.Form):
    fecha = forms.DateField()
    #entrada = forms.IntegerField(Proyeccion)
    combo = forms.IntegerField(Combo)
    #cantidad_entrada = forms.IntegerField()
    
    username = forms.CharField(min_length=5,max_length=20)
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())
    email = forms.EmailField(required =True)
    first_name= forms.CharField(max_length=30, required = True)
    last_name= forms.CharField(max_length=30, required = True)