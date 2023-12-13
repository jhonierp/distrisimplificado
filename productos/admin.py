from django.contrib import admin

# Register your models here.
from productos.models import Producto


@admin.register(Producto)

class ProductoAdmin(admin.ModelAdmin):
    list_display=['id','codigo','nombre','descripcion','categoria','lote_p','imagen','precio','estado','fecha_vencimiento','cantidad']
    
