from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from apps.haypan.api.serializers.serializers import UserTokenSerializer
from rest_framework.views import APIView


class UserToken(APIView):
    def get(self,request,*args,**kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(username=username).first()
            )
            return Response({'token':user_token.key})
        
        except:
            return Response({'error':'credenciales enviadas incorrectas.'},status=status.HTTP_400_BAD_REQUEST)
        




class LoginToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token_instance, created = Token.objects.get_or_create(
                    user=user)
                user_serializer = UserTokenSerializer(user)

                if created:
                    return Response({'token': token_instance.key,
                                    'user': user_serializer.data,
                                    'message': 'inicio de sesion exitoso'}, status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token_instance.delete()  # Corrección aquí
                    token_instance = Token.objects.create(user=user)  # Asignación de nuevo token_instance
                    return Response({'token': token_instance.key,
                                    'user': user_serializer.data,
                                    'message': 'inicio de sesion exitoso'}, status=status.HTTP_201_CREATED)
                    """ return Response({'error':'ya se ha iniciado sesion con este usuario'},status=status.HTTP_409_CONFLICT)"""
            else:
                return Response({'error': 'Este usuario no puede iniciar sesion'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'hola desde response'}, status=status.HTTP_200_OK)


class LogoutToken(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token_key = request.GET.get('token')
            if not token_key:
                return Response({'error': 'Falta el token.'}, status=status.HTTP_400_BAD_REQUEST)

            token = Token.objects.filter(key=token_key).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                session_message = 'Sesiones de usuario eliminadas.'
                token.delete()
                token_message = 'Token eliminado'
                return Response({'token_message': token_message, 'session_message': session_message}, status=status.HTTP_200_OK)
            return Response({'error': 'No se ha encontrado un usuario con estas credenciales.'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': 'No se ha encontrado token en la petición', 'details': str(e)}, status=status.HTTP_409_CONFLICT)