from rest_framework import serializers
from core.models import Contacto

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['nombres', 'apellidos', 'rut', 'telefono','correo','comentario']


