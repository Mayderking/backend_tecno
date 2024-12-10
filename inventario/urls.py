from django.urls import path
from rest_framework import routers
from .views import CategoriaViewSet, ProductoViewSet, VentaViewSet, ClienteViewSet, ProveedorViewSet

router = routers.DefaultRouter()
router.register('Categoria', CategoriaViewSet)
router.register('Productos', ProductoViewSet)
router.register('Proveedor', ProveedorViewSet)
router.register('Venta', VentaViewSet)
router.register('Cliente', ClienteViewSet)

urlpatterns = router.urls