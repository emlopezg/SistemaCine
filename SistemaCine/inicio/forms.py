from django import forms
from django.contrib.auth.models import User
from inicio.models import UserData
#from django.contrib.auth.forms import UserCreationForm
#from django.forms.models import ModelForm

class UserForm(forms.Form):
    username = forms.CharField(label='Usuario', min_length=5,max_length=20, required = True, )
    password = forms.CharField(label='Password', min_length=5, widget=forms.PasswordInput(), required = True)
    email = forms.EmailField(label='Correo',required = True)
    first_name= forms.CharField(label='Nombre', max_length=30, required = True)
    last_name= forms.CharField(label='Apellido',max_length=30, required = True)
    RUC = forms.CharField(label='RUC',required = True)
    cedula = forms.CharField(label='Cedula', required = True)

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado, ingrese otro usuario')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Correo ya registrado, ingrese otra direccion de correo')
        return email
    
    def clean_ruc(self):
        """Comprueba que no exista un email igual en la db"""
        ruc = self.cleaned_data['ruc']
        if UserData.objects.filter(ruc=ruc):
            raise forms.ValidationError('RUC ya registrado, ingrese otro RUC')
        return ruc
    