from django.contrib import admin
# Importar clase jugador
from .models import Jugador, User #usar . para indicar que el archivo se encuentra en la misma aplicacion
# Register your models here.

# Crear un panel de administracion que nos ofrece django
admin.site.register(Jugador)
admin.site.register(User)