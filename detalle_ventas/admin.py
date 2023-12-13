from django.contrib import admin

# Register your models here.
from detalle_ventas.models import Detalle_Venta


@admin.register(Detalle_Venta)

class DetalleVentaAdmin(admin.ModelAdmin):
    list_display=['id','factura_venta','producto_venta','cantidad','precio_producto']
    
