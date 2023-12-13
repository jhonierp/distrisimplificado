from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from factura_compras.models import Factura_Compra
from factura_compras.api.serializers import FacturaComprasSerializer


class FacturaComprasViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=FacturaComprasSerializer
    queryset=Factura_Compra.objects.all()
