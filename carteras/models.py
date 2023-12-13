from django.db import models

# Create your models here.

medio_pago_cartera = (
    ("Efectivo", "Efectivo"),
    ("Tarjeta de Crédito", "Tarjeta de Crédito"),
    ("Transferencia Bancaria", "Transferencia Bancaria"),
)
estado_cartera = (
        ('PENDIENTE', 'Pendiente'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
)

class Cartera(models.Model):
    fecha_facturacion=models.DateTimeField(auto_now_add=True)
    fecha_vencimiento=models.DateField()
    factura_v = models.ForeignKey('factura_ventas.Factura_venta',on_delete=models.SET_NULL,null=True,blank=True)
    medio_pago_cartera=models.CharField(max_length=255,choices=medio_pago_cartera)
    estado_cartera=models.CharField(max_length=255,choices=estado_cartera)
    telefono = models.PositiveIntegerField(null=True)
    
    def __int__(self):
        return self.pago