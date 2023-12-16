from django.db import models

class Cartera(models.Model):
    fecha_vencimiento=models.DateField()
    factura_v = models.ForeignKey('factura_ventas.Factura_venta',on_delete=models.SET_NULL,null=True,blank=True)
    telefono = models.PositiveIntegerField(null=True)
    
    def __int__(self):
        return self.pago
