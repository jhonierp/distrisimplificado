from rest_framework import serializers
from carteras.models import Cartera

class CarterasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cartera
        fields=['id','fecha_facturacion','factura_v','medio_pago_cartera','estado_cartera','fecha_vencimiento','telefono']