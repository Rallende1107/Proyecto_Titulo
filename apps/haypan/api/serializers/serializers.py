from rest_framework import serializers
from apps.haypan.models import Comuna, DetalleReserva, Reserva, Usuario,Producto,Local,Familiar
from django.contrib.auth.hashers import make_password
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','username', 'email', 'first_name', 'last_name', 'apellido_materno', 'direccion', 'comuna', 'rut', 'phone', 'cliente', 'comerciante')


class UserListSerializer(serializers.ModelSerializer):
    class meta:
        model: Usuario

    def to_representation(self, instance):
        return{
            'id': instance['id'],
            'username':instance['username'],
            'first_name':instance['first_name'],
            'last_name':instance['last_name'],
            'apellido_materno':instance['apellido_materno'],
            'direccion':instance['direccion'],
            'password':instance['password'],
            'rut':instance['rut'],
        }


class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = '__all__'



class FamiliaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Familiar
        fields = '__all__'


class LocalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Local
        fields = '__all__'



class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id', 'nombre']

class UserSerializer(serializers.ModelSerializer):
    comuna = serializers.SlugRelatedField(
        slug_field='nombre', queryset=Comuna.objects.all())
    
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'apellido_materno', 'direccion', 'comuna', 'rut', 'phone', 'cliente', 'comerciante']

    def create(self, validated_data):
        # Extraer y eliminar el campo de contraseña para cifrarlo
        password = validated_data.pop('password')
        
        # Cifrar la contraseña antes de crear el usuario
        hashed_password = make_password(password)
        
        # Crear y devolver el usuario con la contraseña cifrada
        usuario = Usuario.objects.create(password=hashed_password, **validated_data)
        return usuario

    def update(self, instance, validated_data):
        # Extraer y eliminar el campo de contraseña para cifrarlo si está presente en los datos validados
        if 'password' in validated_data:
            password = validated_data.pop('password')
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password
        
        return super().update(instance, validated_data)

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'



class DetalleReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleReserva
        fields = '__all__'