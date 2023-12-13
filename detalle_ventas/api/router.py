from rest_framework.routers import DefaultRouter
from detalle_ventas.api.views import DetalleVentasViewSet


route_dventa=DefaultRouter()


route_dventa.register(
    prefix='detalle_venta',basename='detalle_ventas',viewset=DetalleVentasViewSet
    
)
