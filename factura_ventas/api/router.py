from rest_framework.routers import DefaultRouter
from factura_ventas.api.views import FacturaVentasViewSet


route_fventa=DefaultRouter()


route_fventa.register(
    prefix='factura_venta',basename='factura_ventas',viewset=FacturaVentasViewSet
    
)
