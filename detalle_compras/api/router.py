from rest_framework.routers import DefaultRouter
from detalle_compras.api.views import DetalleComprasViewSet


route_dcompra=DefaultRouter()


route_dcompra.register(
    prefix='detalle_compra',basename='detalle_compras',viewset=DetalleComprasViewSet
    
)
