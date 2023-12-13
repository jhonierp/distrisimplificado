from django.db import models

# Create your models here.
class Detalle_Compra(models.Model):
    factura_compra=models.ForeignKey('factura_compras.Factura_Compra',on_delete=models.SET_NULL,null=True,blank=True)
    producto_compra=models.ForeignKey('productos.Producto',on_delete=models.SET_NULL,null=True,blank=True)
    cantidad = models.PositiveIntegerField(null=True)
    precio_unitario=models.DecimalField(max_digits=10,decimal_places=2,null=True)  
    
    def __int__(self):
        return self.producto_compra