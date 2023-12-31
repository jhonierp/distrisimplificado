from rest_framework import serializers
from factura_compras.models import Factura_Compra

class FacturaComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Factura_Compra
        fields=['id','proveedor','telefono','fecha_ingreso','email','categoriaf','medio_pago_c','estado_pago_c','lote_f']
