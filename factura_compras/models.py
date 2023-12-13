from django.db import models

# Create your models here.

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

class Factura_Compra(models.Model):
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    proveedor = models.CharField(max_length=100,null=True)
    telefono = models.CharField(max_length=150)
    medio_pago_c=models.CharField(max_length=255,choices=medio_pago)
    estado_pago_c=models.CharField(max_length=255,choices=estado_pago)
    total_c=models.DecimalField(max_digits=10,decimal_places=2,null=True)  
    
    def __int__(self):
        return self.total_c