from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from factura_ventas.models import Factura_Venta
from factura_ventas.api.serializers import FacturaVentasSerializer


class FacturaVentasViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=FacturaVentasSerializer
    queryset=Factura_Venta.objects.all()
