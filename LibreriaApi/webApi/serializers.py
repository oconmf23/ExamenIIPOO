from rest_framework import serializers 
from webApi.models import TipoLibros, Genero, Estanterias, Clientes, Libros
 
 
class TipoLibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLibros
        fields = ('id','descripcion')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('id','descripcion')

class EstanteriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estanterias
        fields = ('id','numero_Estanterias')

class ClientesSerializer(serializers.ModelSerializer):
    def validate_id(self, value):
        if Clientes.objects.filter(id=value).exists():
            raise serializers.ValidationError('Ya existe un cliente con este numero de identidad')
        return value
    
    class Meta:
        model = Clientes
        fields = ('id','id_card','nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'email', 'id_genero')

class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLibros
        fields = ('id','nombre','autor','numero_Paginas','id_TipoLibros','id_Clientes','id_Estanterias')