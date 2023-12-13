from django.contrib import admin

# Register your models here.
from detalle_compras.models import Detalle_Compra


@admin.register(Detalle_Compra)

class DetalleCompraAdmin(admin.ModelAdmin):
    list_display=['id','factura_compra','producto_compra','cantidad','precio_unitario']
    
