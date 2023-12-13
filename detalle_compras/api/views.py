from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from detalle_compras.models import Detalle_Compra
from detalle_compras.api.serializers import DetalleComprasSerializer


class DetalleComprasViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=DetalleComprasSerializer
    queryset=Detalle_Compra.objects.all()
