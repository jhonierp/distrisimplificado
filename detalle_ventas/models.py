from django.db import models

# Create your models here.
class Detalle_Venta(models.Model):
    factura_venta=models.ForeignKey('factura_ventas.Factura_Venta',on_delete=models.SET_NULL,null=True,blank=True)
    producto_venta=models.ForeignKey('productos.Producto',on_delete=models.SET_NULL,null=True,blank=True)
    cantidad = models.PositiveIntegerField(null=True)
    precio_producto=models.DecimalField(max_digits=10,decimal_places=2,null=True)  
    
    def __int__(self):
        return self.producto_venta