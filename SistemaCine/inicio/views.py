from django.shortcuts import render_to_response
from django.template import RequestContext
from inicio.forms import UserForm
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
from inicio.models import UserData
from xml.dom import UserDataHandler
# Create your views here.

def main(request):
    '''Muestra la pagina de bienvenida y pide al usuario ingresar'''
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def newUser(request):
    '''ABM de usuarios'''
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password= form.cleaned_data['password']
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']
            RUC = form.cleaned_data['RUC']
            cedula = form.cleaned_data['cedula']
            user= User.objects.create_user(username, email, password)
            user.first_name = nombre
            user.last_name = apellido
            user.save()
            userdata = UserData()
            userdata.ruc = RUC
            userdata.cedula = cedula
            userdata.user_id = user.id
            userdata.save()
            return HttpResponseRedirect('/login')
    else:
        data = {}
        form= UserForm(data)
        
    return render_to_response("registrar.html", { 'form' : form  },context_instance=RequestContext(request))