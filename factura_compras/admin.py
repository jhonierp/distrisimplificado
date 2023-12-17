from django.contrib import admin

# Register your models here.
from factura_compras.models import Factura_Compra


@admin.register(Factura_Compra)

class FacturaCompraAdmin(admin.ModelAdmin):
    list_display=['id','proveedor','telefono','fecha_ingreso','email','categoriaf']
    
