from rest_framework.routers import DefaultRouter
from carteras.api.views import CarterasViewSet


route_cartera=DefaultRouter()


route_cartera.register(
    prefix='cartera',basename='carteras',viewset=CarterasViewSet
    
)
