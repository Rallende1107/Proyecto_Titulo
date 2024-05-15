from rest_framework import status
from rest_framework.response import Response
from apps.haypan.models import Usuario
from apps.haypan.api.serializers.serializers import UserSerializer,UserListSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def User_api_view(request):

    if request.method == 'GET':
        Usuarios = Usuario.objects.all().values('id','username','email','first_name','last_name','apellido_materno','direccion','password','rut')
        users_serializer = UserListSerializer(Usuarios, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        users_serializer = UserSerializer(
            data=request.data, status=status.HTTP_201_CREATED)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):
    usuario = Usuario.objects.filter(id=pk).first()

    if usuario:
        if request.method == 'GET':
            user_serializer = UserSerializer(usuario)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            request.data
            usuario = Usuario.objects.filter(id=pk).first()
            user_serializer = UserSerializer(usuario, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            usuario = Usuario.objects.filter(id=pk).first()
            usuario.delete()
            return Response({'message': 'Usuario Eliminado Correctamente!'}, status=status.HTTP_200_OK)


    return Response({'message':'No se ha encontrado un usuario con estos datos'},status= status.HTTP_400_BAD_REQUEST_)
