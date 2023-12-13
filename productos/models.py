from django.db import models
from django.db.models.fields.files import ImageField


# Create your models here.
estado_producto = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('agotado', 'Agotado'),
    ]
class Producto(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    categoria = models.ForeignKey('categorias.Categoria',on_delete=models.SET_NULL,null=True,blank=True)
    lote_p = models.ForeignKey('lotes.Lote',on_delete=models.SET_NULL,null=True,blank=True)
    precio=models.DecimalField(max_digits=10,decimal_places=2,null=True) 
    fecha_vencimiento = models.DateField()
    imagen= models.ImageField(upload_to='producto', null=True)
    estado=models.CharField(max_length=255,choices=estado_producto,null=True)
    cantidad = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return self.nombre
