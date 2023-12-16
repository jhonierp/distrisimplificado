from django.contrib import admin

# Register your models here.
from carteras.models import Cartera


@admin.register(Cartera)

class CarteraAdmin(admin.ModelAdmin):
    list_display=['id','factura_v','medio_pago_cartera','estado_cartera','fecha_vencimiento','telefono']
    
