from django import forms
from cinema.models import Proyeccion, Horario
#no me acuerdo para que cree este xDDD
class ProyeccionForm(forms.Form):
    pelicula = forms.ModelChoiceField(Proyeccion, label=u'pelicula', queryset=Proyeccion.objects.all())
    fecha = forms.ModelChoiceField(initial=Proyeccion.desde,)
    hora = forms.ModelChoiceField(Horario,label=u'horario', queryset=Horario.objects.all())