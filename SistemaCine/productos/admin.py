from django.contrib import admin
from models import Producto, ProductoFinal

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo','producto','proveedor', 'stock')
    readonly_fields = ('stock',)

class ProductoFinalAdmin(admin.ModelAdmin):
    list_display = ('codigo','descripcion')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoFinal, ProductoFinalAdmin)

