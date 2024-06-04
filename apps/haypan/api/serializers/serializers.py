from rest_framework import serializers
from apps.haypan.models import Comuna, DetalleReserva, Reserva, Usuario,Producto,Local,Familiar
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario
    
    def update(self, instance, validated_data):
        update_user =super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

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

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'apellido_materno', 'direccion', 'comuna', 'rut', 'phone', 'cliente', 'comerciante']


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'



class DetalleReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleReserva
        fields = '__all__'

