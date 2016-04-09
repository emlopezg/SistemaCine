from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
#from django.forms.models import ModelForm

class UserForm(forms.Form):
    username = forms.CharField(min_length=5,max_length=20)
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())
    email = forms.EmailField(required =True)
    first_name= forms.CharField(max_length=30, required = True)
    last_name= forms.CharField(max_length=30, required = True)

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