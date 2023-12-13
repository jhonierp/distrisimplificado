from django.contrib import admin

# Register your models here.
from stock.models import Stock


@admin.register(Stock)

class StockAdmin(admin.ModelAdmin):
    list_display=['id','producto_stock','lote_stock']
    
