from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from productos.models import Producto
from productos.api.serializers import ProductosSerializer
#filtro
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductosViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=ProductosSerializer
    queryset=Producto.objects.all()
    #filtro
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    filterset_fields=['categoria']
    ordening_fields='__all__'
    