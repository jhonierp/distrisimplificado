from rest_framework import serializers
from lotes.models import Lote

class LotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lote
        fields=['id','fecha_ingreso','numero_lote']