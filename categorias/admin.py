from django.contrib import admin

# Register your models here.
from categorias.models import Categoria


@admin.register(Categoria)

class ProductoAdmin(admin.ModelAdmin):
    list_display=['id','descripcion']
    
