from django.db import models

medio_pago = (
    ("Efectivo", "Efectivo"),
    ("Tarjeta de Crédito", "Tarjeta de Crédito"),
    ("Transferencia Bancaria", "Transferencia Bancaria"),
)
estado_pago = (
        ('PENDIENTE', 'Pendiente'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
)
# Create your models here.
class Factura_Venta(models.Model):
    
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=100,null=True)
    medio_pago_v=models.CharField(max_length=255,choices=medio_pago)
    estado_pago_v=models.CharField(max_length=255,choices=estado_pago)
   
    
    def __int__(self):
        return self.total_v
