from django.contrib import admin
from bancos.models import Banco,CuentaCorriente, Cheque,Chequera
# Register your models here.

class CuentaCorrienteAdmin(admin.ModelAdmin):
    list_display = ('codigocuenta', 'saldo')

class ChequeraAdmin(admin.ModelAdmin):
    list_display = ('codigochequera', 'rangoini','rangofin')

class ChequeAdmin(admin.ModelAdmin):
    list_display = ('serie','monto')

admin.site.register(Banco)
admin.site.register(Chequera, ChequeraAdmin)
admin.site.register(Cheque, ChequeAdmin)
admin.site.register(CuentaCorriente, CuentaCorrienteAdmin)

