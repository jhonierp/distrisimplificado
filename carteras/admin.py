from django.contrib import admin

# Register your models here.
from carteras.models import Cartera


@admin.register(Cartera)

class CarteraAdmin(admin.ModelAdmin):
    list_display=['id','factura_v','fecha_vencimiento','telefono']
    
