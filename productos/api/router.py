from rest_framework.routers import DefaultRouter
from productos.api.views import ProductosViewSet


route_producto=DefaultRouter()


route_producto.register(
    prefix='productos',basename='productos',viewset=ProductosViewSet
    
)
