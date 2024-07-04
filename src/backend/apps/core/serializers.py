from rest_framework import serializers
from apps.core.models import Persona, Empresa, GrupoTrabajo, Personal, Producto

class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    f_nacimiento=serializers.CharField()
    ciudad = serializers.CharField()
    avatar = serializers.FileField()
    class Meta:
        model = Persona 

#mio
# <- ------------------------------------------------------------------------------------------- ->

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'user', 'nombre_empresa']

class GrupoTrabajoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer()

    class Meta:
        model = GrupoTrabajo
        fields = ['id', 'nombre_grupo', 'categoria', 'empresa']

class PersonalSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    grupos_trabajo = GrupoTrabajoSerializer(many=True)

    class Meta:
        model = Personal
        fields = ['id', 'user', 'nombre', 'grupos_trabajo']

class ProductoSerializer(serializers.ModelSerializer):
    grupo_trabajo = GrupoTrabajoSerializer()

    class Meta:
        model = Producto
        fields = ['id', 'nombre_producto', 'descripcion_producto', 'precio_producto', 'categoria_producto', 'grupo_trabajo']

    
"""
class ProductoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre_producto = serializers.CharField()
    cantidad_producto = serializers.IntegerField()
    precio_producto = serializers.IntegerField()
    categoria_producto = serializers.CharField()
    class Meta:
        model = Producto
"""