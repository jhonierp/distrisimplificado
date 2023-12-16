from django.db import models

medio_pago = (
    ("Efectivo", "Efectivo"),
    ("Transferencia BANCOLOMBIA", "Transferencia BANCOLOMBIA"),
    ("Transferencia NEQUI", "Transferencia NEQUI"),
)
estado_pago = (
        ('PENDIENTE', 'Pendiente'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
)
# Create your models here.
class Factura_Venta(models.Model):
    
    fecha_ingreso= models.DateField()
    cliente = models.CharField(max_length=100,null=True)
    medio_pago_v=models.CharField(max_length=255,choices=medio_pago)
    estado_pago_v=models.CharField(max_length=255,choices=estado_pago)
   
    
    def __int__(self):
        return self.total_v
