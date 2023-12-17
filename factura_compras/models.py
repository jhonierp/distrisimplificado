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
    fecha_ingreso=models.DateField()
    proveedor = models.CharField(max_length=100,null=True)
    telefono = models.CharField(max_length=150)
    email = models.CharField(max_length=100,null=True)
    categoriaf = models.ForeignKey('categorias.Categoria',on_delete=models.SET_NULL,null=True,blank=True)
    medio_pago_c=models.CharField(max_length=255,choices=medio_pago)
    estado_pago_c=models.CharField(max_length=255,choices=estado_pago)
    lote_f = models.ForeignKey('lotes.Lote',on_delete=models.SET_NULL,null=True,blank=True)
    
    def __int__(self):
        return self.total_c
