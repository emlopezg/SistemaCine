from django.contrib import admin
from models import Producto, ProductoFinal, Combo, Proveedor

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo','producto','proveedor', 'stock')
    readonly_fields = ('stock',)

class ProductoFinalAdmin(admin.ModelAdmin):
    list_display = ('codigo','descripcion','volumen')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('proveedor','tel_fijo','tel_celular','direccion')

class ComboAdmin(admin.ModelAdmin):
    list_display = ('codigo','descripcion','precio')
    filter_horizontal = ('producto','productofinal')
    
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoFinal, ProductoFinalAdmin)
admin.site.register(Combo, ComboAdmin)
admin.site.register(Proveedor, ProveedorAdmin)

