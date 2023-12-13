from django.contrib import admin

# Register your models here.
from lotes.models import Lote


@admin.register(Lote)

class ProductoAdmin(admin.ModelAdmin):
    list_display=['id','fecha_ingreso','numero_lote']
    
