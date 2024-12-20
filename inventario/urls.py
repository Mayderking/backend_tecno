from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    CategoriaViewSet, ProductoViewSet, VentaViewSet,
    ProveedorViewSet, signup
)

router = routers.DefaultRouter()
router.register('Categoria', CategoriaViewSet)
router.register('Producto', ProductoViewSet)
router.register('Proveedor', ProveedorViewSet)
router.register('Venta', VentaViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("signup/", signup, name="signup"),
] + router.urls 