from rest_framework import serializers
from carteras.models import Cartera

class CarterasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cartera
        fields=['id','factura_v','fecha_vencimiento','telefono']
