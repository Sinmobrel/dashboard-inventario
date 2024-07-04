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
        fields = ['id', 'username', 'password', 'nombre_empresa']

class GrupoTrabajoSerializer(serializers.ModelSerializer):
    empresa = serializers.PrimaryKeyRelatedField(queryset=Empresa.objects.all())

    class Meta:
        model = GrupoTrabajo
        fields = ['id', 'categoria', 'empresa']

class PersonalSerializer(serializers.ModelSerializer):
    grupos_trabajo = serializers.PrimaryKeyRelatedField(many=True, queryset=GrupoTrabajo.objects.all())

    class Meta:
        model = Personal
        fields = ['id', 'username', 'password', 'nombre', 'grupos_trabajo']

class ProductoSerializer(serializers.ModelSerializer):
    grupo_trabajo = serializers.PrimaryKeyRelatedField(queryset=GrupoTrabajo.objects.all())

    class Meta:
        model = Producto
        fields = ['id', 'nombre_producto', 'cantidad_producto', 'precio_producto', 'grupo_trabajo']