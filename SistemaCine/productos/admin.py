from django.contrib import admin
from models import Producto, ProductoFinal

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo','producto','proveedor', 'stock')
    readonly_fields = ('stock',)

class ProductoUnitarioAdmin(admin.ModelAdmin):
    list_display = ('codigo','producto','descripcion', 'precio')
    readonly_fields = ('stock',)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoFinal, ProductoUnitarioAdmin)

