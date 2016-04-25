from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserData(models.Model):
    user = models.OneToOneField(User)
    ruc = models.CharField(max_length=15, help_text = 'Ingrese el ruc del usuario')
    cedula = models.CharField(max_length=10, help_text = 'Ingrese la cedula del usuario')
    
    def __unicode__(self):
        return self.user.username
    
    '''def create_userdata(self, ruc, cedula, user, **extra_fields):
        return self._create_user(ruc, cedula, user, **extra_fields)'''