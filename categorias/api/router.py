from rest_framework.routers import DefaultRouter
from categorias.api.views import CategoriasViewSet


route_categoria=DefaultRouter()


route_categoria.register(
    prefix='categorias',basename='categorias',viewset=CategoriasViewSet
    
)
