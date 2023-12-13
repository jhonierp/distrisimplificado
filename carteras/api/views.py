from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from carteras.models import Cartera
from carteras.api.serializers import CarterasSerializer


class CarterasViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=CarterasSerializer
    queryset=Cartera.objects.all()
