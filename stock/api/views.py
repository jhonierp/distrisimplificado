from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from stock.models import Stock
from stock.api.serializers import StockSerializer


class StockViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=StockSerializer
    queryset=Stock.objects.all()

    