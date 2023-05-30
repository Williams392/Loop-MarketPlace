# (1) views.py
from rest_framework.parsers import MultiPartParser, FormParser  # img

from django.shortcuts import get_object_or_404  # hoy


from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication  # NO
from rest_framework.permissions import IsAuthenticated
from authentication.serializers import UserSerializer

from .models import Product
from .serializers import ProductSerializer


class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class ProductListView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # img
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get_object(self, pk_product):
    #     return get_object_or_404(Product, pk=pk_product)

    def get(self, request, pk_product=None):
        if pk_product:
            product = get_object_or_404(Product, pk=pk_product)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_product=None):
        if pk_product:
            product = get_object_or_404(Product, pk=pk_product)
            product.delete()
            return Response({"msg": f"Producto con ID {pk_product} ha sido eliminado"})
        else:
            return Response({"msg": "Necesitas enviar el ID del producto a eliminar"}, status=status.HTTP_400_BAD_REQUEST)


""""
Paso 5:

. Creando una vista PROTEGIDA:
  _ Para solo mostrar al dueño del proveerdor, el desorrollador, etc.
    . Para ver la lista de ventas, etc.
    
    
. class ProtectedView:
_ solicitud GET para la ruta 'products/'. Devuelve todos los productos 
almacenados en la base de datos en formato JSON.

. class ProductDetailView

"""
