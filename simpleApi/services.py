from .models import Usuario, Puntaje

class UsuarioService:
    def find_or_create(self, nombre, edad):
        return Usuario.objects.find_or_create(nombre=nombre, edad=edad)

class PuntajeService:
    def guardar_puntaje(self, puntaje_data):
        puntaje = Puntaje.objects.create(**puntaje_data)
        return puntaje

    def obtener_todos_puntajes(self):
        return Puntaje.objects.all()
