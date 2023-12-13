from rest_framework import serializers
from categorias.models import Categoria

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields=['id','descripcion']