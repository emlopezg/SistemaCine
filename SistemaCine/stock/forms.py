from django import forms
from cinema.models import Proyeccion, Horario
from productos.models import Combo

class CompraForm(forms.Form):
    '''FECHA_CHOICES = (
    (1, "2016-05-09" ),
    (2, "2016-05-10"),
    (3, "2016-05-11"),
    (4, "2016-05-12"),
    (5, "2016-05-13")
    )'''
    pelicula = forms.ModelChoiceField(Proyeccion.objects.all())
    cantidadmenores = forms.IntegerField(initial = 0)
    cantidadmayores = forms.IntegerField(initial = 0)
    asientos_reservados = forms.CharField(max_length=20)
    #nroasiento = forms.IntegerField()
    #fecha = forms.ModelChoiceField(initial=Proyeccion.desde,)
    #fecha = forms.ChoiceField(choices = FECHA_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    fecha = forms.DateField()
    hora = forms.ModelChoiceField(Horario.objects.all())
    #hora = forms.ModelChoiceField(Horario,label=u'horario', queryset=Horario.objects.all())
    #entrada = forms.IntegerField(Proyeccion)
    combo = forms.ModelChoiceField(Combo.objects.all(),required=False, initial = "Combo Hexa")
    #combo1 = forms.FileField(Combo.objects.all, required = False, widget=forms.RadioSelect())
