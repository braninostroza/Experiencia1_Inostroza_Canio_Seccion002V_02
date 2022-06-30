from rest_framework import serializers
from core.models import Registro

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['nombre', 'correo', 'contraseña']


