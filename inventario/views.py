from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.contrib.auth.models import User
from .serializer import CategoriaSerializer, ProductoSerializer, VentaSerializer
from .models import Categoria, Producto, Venta


# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({"message": "Login exitoso"})
    return JsonResponse({"error": "Credenciales inválidas"}, status=403)

@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if not username or not password or not email:
        return Response(
            {"error": "Todos los campos son obligatorios."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "El nombre de usuario ya está en uso."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "Usuario registrado con éxito."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(
            {"error": f"Error al registrar el usuario: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

class CategoriaViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class ProductoViewSet(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    @action(detail=False, methods=['get'], url_path='por-categoria/(?P<categoria_id>\d+)')
    def productos_por_categoria(self, request, categoria_id=None):
        productos = Producto.objects.filter(categoria_id=categoria_id)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class VentaViewSet(ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()

