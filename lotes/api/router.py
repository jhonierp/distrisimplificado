from rest_framework.routers import DefaultRouter
from lotes.api.views import LotesViewSet


route_lote=DefaultRouter()


route_lote.register(
    prefix='lotes',basename='lotes',viewset=LotesViewSet
    
)
