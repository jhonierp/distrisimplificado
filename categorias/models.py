from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Categoria(models.Model):
    descripcion= models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.descripcion
