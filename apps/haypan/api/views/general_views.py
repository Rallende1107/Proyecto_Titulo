from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from apps.haypan.models import Comuna, DetalleReserva, Producto,Local,Familiar, Reserva,Usuario
from apps.haypan.api.serializers.serializers import ComunaSerializer, DetalleReservaSerializer, ProductoSerializer,FamiliaSerializer,LocalSerializer, ReservaSerializer,UserSerializer
from apps.haypan.api.authentication_mixins import Authenticacion

class DetalleReservaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DetalleReservaSerializer
    queryset = DetalleReserva.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Detalle Reserva creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class DetalleReservaRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = DetalleReservaSerializer

    def get_queryset(self):
        return DetalleReserva.objects.all()

    def delete(self, request, pk=None, *args, **kwargs):
        detalle_reserva = self.get_object(pk)
        if detalle_reserva:
            detalle_reserva.delete()
            return Response({'message': 'Detalle Reserva eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un detalle Reserva con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):
        detalle_reserva = self.get_object(pk)
        if not detalle_reserva:
            return Response({'error': 'No existe un detalle Reserva con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(detalle_reserva, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        detalle_reserva = self.get_object(pk)
        if not detalle_reserva:
            return Response({'error': 'No existe un detalle Reserva con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(detalle_reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return DetalleReserva.objects.get(pk=pk)
        except DetalleReserva.DoesNotExist:
            return None

class DetalleReservaViews(viewsets.ModelViewSet):
    serializer_class = DetalleReservaSerializer
    queryset = DetalleReserva.objects.all()

class ReservaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReservaSerializer
    queryset = ReservaSerializer.Meta.model.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': ' Reserva creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
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


class ProductoViews(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = ProductoSerializer.Meta.model.objects.all()

class ProductoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer
    queryset = ProductoSerializer.Meta.model.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

        nueva_cantidad = request.data.get('cantidad', None)
        if nueva_cantidad is not None:
            try:
                nueva_cantidad = int(nueva_cantidad)
                if nueva_cantidad < 0 and producto.cantidad + nueva_cantidad < 0:
                    return Response({'error': 'Cantidad insuficiente en el stock'}, status=status.HTTP_400_BAD_REQUEST)
                producto.cantidad += nueva_cantidad
                producto.save()
            except ValueError:
                return Response({'error': 'Cantidad no válida'}, status=status.HTTP_400_BAD_REQUEST)

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
