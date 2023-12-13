from django.db import models

# Create your models here.
class Stock(models.Model):
    producto_stock=models.ForeignKey('productos.Producto',on_delete=models.SET_NULL,null=True,blank=True)
    lote_stock=models.ForeignKey('lotes.Lote',on_delete=models.SET_NULL,null=True,blank=True)
    
    def __int__(self):
        return self.cantidad