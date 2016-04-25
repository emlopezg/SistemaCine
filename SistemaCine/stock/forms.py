from django import forms
from cinema.models import Proyeccion
from productos.models import Combo

class CompraForm(forms.Form):
    #entrada = forms.IntegerField(Proyeccion)
    combo = forms.ModelChoiceField(Combo.objects.all(),required=False, initial = "Combo Hexa")
    #combo1 = forms.FileField(Combo.objects.all, required = False, widget=forms.RadioSelect())