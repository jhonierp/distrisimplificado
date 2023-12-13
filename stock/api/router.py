from rest_framework.routers import DefaultRouter
from stock.api.views import StockViewSet


route_stock=DefaultRouter()


route_stock.register(
    prefix='stock',basename='stock',viewset=StockViewSet
    
)
