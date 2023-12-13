from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from lotes.models import Lote
from lotes.api.serializers import LotesSerializer


class LotesViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=LotesSerializer
    queryset=Lote.objects.all()