from rest_framework import viewsets
from .models import Usuario, Puntaje
from .serializers import UsuarioSerializer, PuntajeSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PuntajeViewSet(viewsets.ModelViewSet):
    queryset = Puntaje.objects.all()
    serializer_class = PuntajeSerializer
