from django.contrib import admin

# Register your models here.
from factura_ventas.models import Factura_Venta


@admin.register(Factura_Venta)

class FacturaVentaAdmin(admin.ModelAdmin):
    list_display=['id','cliente','fecha_ingreso','medio_pago_v','estado_pago_v']
    
