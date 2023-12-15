from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from detalle_ventas.models import Detalle_Venta
from detalle_ventas.api.serializers import DetalleVentasSerializer

#filtro
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class DetalleVentasViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=DetalleVentasSerializer
    queryset=Detalle_Venta.objects.all()
#filtro
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    filterset_fields=['factura_venta']
    ordening_fields='__all__'
    