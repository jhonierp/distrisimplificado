from django.db import models

# Create your models here.

class Lote(models.Model):
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    numero_lote = models.PositiveIntegerField(null=True)
    
    
    def __int__(self):
        return self.numero_lote