from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from apps.haypan.models import Producto,Local,Familiar
from apps.haypan.api.serializers.serializers import ProductoSerializer,FamiliaSerializer,LocalSerializer




class ProductoViews(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = ProductoSerializer.Meta.model.objects.all()









class ProductoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer
    queryset = ProductoSerializer.Meta.model.objects.all()

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.sava()
            return Response ({'message': 'Producto creado correctammente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 

class ProductoListAPIView(generics.ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.all()

class ProductoCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductoSerializer

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.sava()
            return Response ({'message': 'Producto creado correctammente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 

class ProductoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def delete(self, request, pk=None):
        producto = self.get_queryset().filter(id=pk).first()
        if producto:
            producto.state = False
            producto.save()
            return Response({'message': 'Producto eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un Producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            producto = self.get_queryset().get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'No existe un Producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            producto = self.get_queryset().get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'No existe un Producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Vista para recuperar un producto específico
class ProductoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductoSerializer

    # Define el queryset utilizado para recuperar el producto
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

# Vista para eliminar un producto específico
class ProductoDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductoSerializer

    # Define el queryset utilizado para recuperar el producto
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    # Método para manejar la eliminación del producto
    def delete(self, request, pk=None):
        producto = self.get_queryset().filter(id=pk).first()
        if producto:
            producto.state = False  # Marca el producto como inactivo en lugar de eliminarlo
            producto.save()
            return Response({'message': 'Producto eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un Producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

# Vista para actualizar un producto específico
class ProductoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductoSerializer

    # Define el queryset utilizado para recuperar el producto
    def get_queryset(self):
        return Producto.objects.all()

    # Método para manejar la actualización parcial del producto (PATCH)
    def patch(self, request, pk=None):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'No existe un Producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método para manejar la actualización completa del producto (PUT)
    def put(self, request, pk=None):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'No existe un Producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class FamiliaListAPIView(generics.ListAPIView):
    serializer_class = FamiliaSerializer

    def get_queryset(self):
        return Familiar.objects.all()



class LocalListAPIView(generics.ListAPIView):
    serializer_class = LocalSerializer

    def get_queryset(self):
        return Local.objects.all()


