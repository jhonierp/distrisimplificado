from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from categorias.models import Categoria
from categorias.api.serializers import CategoriasSerializer


class CategoriasViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=CategoriasSerializer
    queryset=Categoria.objects.all()