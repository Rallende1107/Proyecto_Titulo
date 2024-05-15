from rest_framework import serializers
from apps.haypan.models import Usuario,Producto,Local,Familiar

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