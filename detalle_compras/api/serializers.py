from rest_framework import serializers
from detalle_compras.models import Detalle_Compra

from factura_compras.api.serializers import FacturaComprasSerializer


class DetalleComprasSerializer(serializers.ModelSerializer):
    fcompra_data=FacturaComprasSerializer(source='factura_compra',read_only=True)
    class Meta:
        model=Detalle_Compra
        fields=['id','factura_compra','fcompra_data','producto_compra','cantidad','precio_unitario']