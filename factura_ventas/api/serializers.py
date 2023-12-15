from rest_framework import serializers
from factura_ventas.models import Factura_Venta

class FacturaVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Factura_Venta
        fields=['id','cliente','fecha_ingreso','medio_pago_v','estado_pago_v']
