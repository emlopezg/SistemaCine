from django.shortcuts import render_to_response
from django.template import RequestContext
from inicio.forms import UserForm
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def main(request):
    '''Muestra la pagina de bienvenida y pide al usuario ingresar'''
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def newUser(request):
    '''ABM de usuarios'''
    if request.method == 'POST':
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
        
    return render_to_response("registrar.html", { 'form' : form  },context_instance=RequestContext(request))