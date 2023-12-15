from rest_framework import serializers
from detalle_ventas.models import Detalle_Venta


class DetalleVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Detalle_Venta
        fields=['id','factura_venta','producto_venta','cantidad']
