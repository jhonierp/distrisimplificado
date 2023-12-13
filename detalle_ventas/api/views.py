from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from detalle_ventas.models import Detalle_Venta
from detalle_ventas.api.serializers import DetalleVentasSerializer


class DetalleVentasViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=DetalleVentasSerializer
    queryset=Detalle_Venta.objects.all()
