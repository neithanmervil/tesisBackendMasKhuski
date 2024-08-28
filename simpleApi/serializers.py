from rest_framework import serializers
from .models import Usuario, Puntaje

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PuntajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntaje
        fields = '__all__'
