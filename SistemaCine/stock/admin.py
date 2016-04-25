from django.contrib import admin
from stock.models import OrdenDeCompra

# Register your models here.

class OrdenDeCompraAdmin(admin.ModelAdmin):
    list_display = ('producto','proveedor', 'cantidad_producto','aprobado','estado')


admin.site.register(OrdenDeCompra,OrdenDeCompraAdmin)
