from rest_framework.routers import DefaultRouter
from factura_compras.api.views import FacturaComprasViewSet


route_fcompra=DefaultRouter()


route_fcompra.register(
    prefix='factura_compra',basename='factura_compras',viewset=FacturaComprasViewSet
    
)
