from django.db import models

# Create your models here.



class Factura_Compra(models.Model):
    fecha_ingreso=models.DateField()
    proveedor = models.CharField(max_length=100,null=True)
    telefono = models.CharField(max_length=150)
    email = models.CharField(max_length=100,null=True)
    
    
    def __int__(self):
        return self.total_c
