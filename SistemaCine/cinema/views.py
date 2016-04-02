from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from models import Pelicula


class PeliculaList(ListView):
    """
    Metodo para listar los datos de clientes registrados en el sistema
    """
    model = Pelicula


class PeliculaCreate(CreateView):
    """
    Metodo para crear registros de clientes en el sistema
    """    
    model = Pelicula
    fields = ['nombre', 'duracion', 'director']
    success_url = reverse_lazy('cinema:pelicula_list')


class PeliculaUpdate(UpdateView):
    """
    Metodo para modificar datos de clientes en el sistema
    """
    model = Pelicula
    fields = ['nombre', 'duracion', 'director']
    success_url = reverse_lazy('cinema:pelicula_list')


class PeliculaDelete(DeleteView):
    """
    Metodo para eliminar definitivamente datos de clientes del sistema
    """    
    model = Pelicula
    success_url = reverse_lazy('cinema:pelicula_list')
