
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.router import route_user
from lotes.api.router import route_lote
from productos.api.router import route_producto
from categorias.api.router import route_categoria
from stock.api.router import route_stock
from factura_compras.api.router import route_fcompra
from detalle_compras.api.router import route_dcompra
from factura_ventas.api.router import route_fventa
from detalle_ventas.api.router import route_dventa
from carteras.api.router import route_cartera


from django.conf import settings
from django.conf.urls.static import static

"""generador de token"""
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from . import views


schema_view = get_schema_view(
   openapi.Info(
      title="API distritiendamj",
      default_version='v1',
      description="Documentación Api distritiendamj",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="wilson.199819@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
from users.models import User

urlpatterns = [
   path('imagenes/producto/<str:image_name>/', views.product_image_view, name='product_image'),
   path('imagenes/producto/<str:image_name>', views.product_image_view), # Add the same pattern without the trailing slash
   path('admin/', admin.site.urls),
   path('documentacionapi<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('documentacionapi/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api',include('users.api.router')),
   path('',include(route_user.urls)),
   path('',include(route_lote.urls)),
   path('',include(route_producto.urls)),
   path('',include(route_categoria.urls)),
   path('',include(route_stock.urls)),
   path('',include(route_fcompra.urls)),
   path('',include(route_dcompra.urls)),
   path('',include(route_fventa.urls)),
   path('',include(route_dventa.urls)),
   path('',include(route_cartera.urls)),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
