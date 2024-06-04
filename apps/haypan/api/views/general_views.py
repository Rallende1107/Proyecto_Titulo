from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from apps.haypan.models import Comuna, DetalleReserva, Producto,Local,Familiar, Reserva,Usuario
from apps.haypan.api.serializers.serializers import ComunaSerializer, DetalleReservaSerializer, ProductoSerializer,FamiliaSerializer,LocalSerializer, ReservaSerializer,UserSerializer
from apps.haypan.api.authentication_mixins import Authenticacion




class DetalleReservaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DetalleReservaSerializer
    queryset = DetalleReservaSerializer.Meta.model.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Detalle Reserva creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class  DetalleReservaRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = DetalleReservaSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def delete(self, request, pk=None):
        detalleReserva = self.get_queryset().filter(id=pk).first()
        if detalleReserva:
            detalleReserva.state = False
            detalleReserva.save()
            return Response({'message': 'detalle Reserva eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un detalle Reserva  con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            detalleReserva = self.get_queryset().get(pk=pk)
        except DetalleReserva.DoesNotExist:
            return Response({'error': 'No existe un detalle Reserva con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(detalleReserva, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            detalleReserva = self.get_queryset().get(pk=pk)
        except detalleReserva.DoesNotExist:
            return Response({'error': 'No existe un reserva con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(detalleReserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleReservaViews(viewsets.ModelViewSet):
    serializer_class = DetalleReservaSerializer
    queryset = DetalleReservaSerializer.Meta.model.objects.all()


class ReservaRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = ReservaSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def delete(self, request, pk=None):
        reserva = self.get_queryset().filter(id=pk).first()
        if reserva:
            reserva.state = False
            reserva.save()
            return Response({'message': 'reserva eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un reserva con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            reserva = self.get_queryset().get(pk=pk)
        except Reserva.DoesNotExist:
            return Response({'error': 'No existe un reserva con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(reserva, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            reserva = self.get_queryset().get(pk=pk)
        except reserva.DoesNotExist:
            return Response({'error': 'No existe un reserva con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservaViews(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    queryset = ReservaSerializer.Meta.model.objects.all()

class LocalListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LocalSerializer
    queryset = LocalSerializer.Meta.model.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Local creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class LocalRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = LocalSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def delete(self, request, pk=None):
        local = self.get_queryset().filter(id=pk).first()
        if local:
            local.state = False
            local.save()
            return Response({'message': 'Local eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un Local con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            local = self.get_queryset().get(pk=pk)
        except Local.DoesNotExist:
            return Response({'error': 'No existe un local con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(local, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            local = self.get_queryset().get(pk=pk)
        except Local.DoesNotExist:
            return Response({'error': 'No existe un local con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(local, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocalViews(viewsets.ModelViewSet):
    serializer_class = LocalSerializer
    queryset = LocalSerializer.Meta.model.objects.all()






class UserListCreateAPIView( generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.sava()
            return Response ({'message': 'Usuario creado correctammente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 

class UserRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def delete(self, request, pk=None):
        usuario = self.get_queryset().filter(id=pk).first()
        if usuario:
            usuario.state = False
            usuario.save()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un Usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            usuario = self.get_queryset().get(pk=pk)
        except usuario.DoesNotExist:
            return Response({'error': 'No existe un Usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            usuario = self.get_queryset().get(pk=pk)
        except usuario.DoesNotExist:
            return Response({'error': 'No existe un Usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(Usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioViews(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()






class ProductoViews(Authenticacion,viewsets.ModelViewSet):
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




class FamiliaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FamiliaSerializer
    queryset = FamiliaSerializer.Meta.model.objects.all()
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.sava()
            return Response ({'message': 'Local creado correctammente'},status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 

class FamiliaRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = FamiliaSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def delete(self, request, pk=None):
        familia = self.get_queryset().filter(id=pk).first()
        if familia:
            familia.state = False
            familia.save()
            return Response({'message': 'Familia eliminada correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una Familia con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            familia = self.get_queryset().get(pk=pk)
        except Familiar.DoesNotExist:
            return Response({'error': 'No existe una Familia con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(familia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            familia = self.get_queryset().get(pk=pk)
        except Familiar.DoesNotExist:
            return Response({'error': 'No existe una Familia con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(familia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FamiliaViews(viewsets.ModelViewSet):
    serializer_class = FamiliaSerializer
    queryset = FamiliaSerializer.Meta.model.objects.all()



class ComunaViews(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        # Crear una lista de nombres de comunas
        comunas_nombres = [comuna['nombre'] for comuna in serializer.data]
        return Response(comunas_nombres)
