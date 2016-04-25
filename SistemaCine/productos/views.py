from django.shortcuts import render
from productos.models import Combo
# Create your views here.
from django.views.generic import TemplateView,ListView

class ComboList(ListView):
    model = Combo