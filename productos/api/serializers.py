from rest_framework import serializers
from productos.models import Producto

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields=['id','codigo','nombre','descripcion','categoria','lote_p','imagen','precio','estado','fecha_vencimiento','cantidad']
