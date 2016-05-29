from django.contrib import admin
from stock.models import OrdenDeCompra, ReservaAsiento, Pago, Recepcion, Registro
from . import models

# Register your models here.

class PagoAdmin(admin.ModelAdmin):
    list_display = ('proveedor','estado','total')
    list_filter = ('proveedor',)
    readonly_fields = ('ordencompra','proveedor','total','tipopago',)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario','proyeccion', 'fechafuncion','horario','total','pagado')
    class Media:
        js = ('/static/admin/js/hide_attribute.js',)


class OrdenDeCompraAdmin(admin.ModelAdmin):
    list_display = ('producto','proveedor', 'cantidad_producto','aprobado','estado',)
    class Media:
        js = ('/static/admin/js/hide_attribute.js',)
    
    '''def get_readonly_fields(self, request, obj=None):
        return ('fechafactura', 'factura')'''

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'concepto','ingreso','egreso',)
    readonly_fields = ('concepto', 'fecha', 'ingreso','egreso',)

class RecepcionAdmin(admin.ModelAdmin):
    list_display = ('numerofactura', 'proveedor','producto', 'cantidadrecibida','fecharecepcion',)
    #readonly_fields = ('concepto', 'fecha', 'ingreso','egreso',)

admin.site.register(OrdenDeCompra,OrdenDeCompraAdmin)
admin.site.register(Recepcion, RecepcionAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(ReservaAsiento, ReservaAdmin)
admin.site.register(Registro, RegistroAdmin)



'''
class OrdenDeCompraInLine(admin.TabularInline):
    model = models.OrdenDeCompra
    #list_display = ("fecha","producto","cantidad")
    extra = 0
 
 
#@admin.register(models.Profile)
class ProveedorAdmin(admin.ModelAdmin):
 
    list_display = ("producto",)
 
    #search_fields = ["user__username"]
 
    inlines = [
        OrdenDeCompraInLine
    ]
 
    def _orden(self, obj):
        return obj.ordendecompras.all().count()

admin.site.register(Proveedor,ProveedorAdmin)    '''