from django.db import models

class UsuarioManager(models.Manager):
    def find_by_nombre_and_edad(self, nombre, edad):
        return self.get_queryset().filter(nombre=nombre, edad=edad).first()

    def find_or_create(self, nombre, edad):
        usuario = self.find_by_nombre_and_edad(nombre, edad)
        if usuario is None:
            usuario = self.create(nombre=nombre, edad=edad)
        return usuario

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    objects = UsuarioManager()

    def __str__(self):
        return f'{self.nombre} ({self.edad} años)'

class Puntaje(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=50)
    puntos = models.IntegerField()
    tiempo = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.puntos} puntos'