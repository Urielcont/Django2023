from django.urls import path
from . import views
# Crear urls de la aplicaion
urlpatterns = [
    path('', views.home), #definir ruta llamando la funcion de views.py
    path('login/', views.login,), #ruta para el login
    path('login/validar/', views.sesion,), #ruta para mandar validar el login
    path('login/listar/', views.listar), #ruta incial de lado admin
    path('login/gestion/', views.gestionar), #ruta del formulario pora agregar nuevo jugador
    path('login/listar/registrar/', views.registrar), #ruta para enviar datos del registrado
    path('login/listar/editar/<codigo>', views.editar), #ruta para mandar el codigo de editar
    path('login/listar/eliminar/<codigo>', views.eliminar), #ruta para eliminar jugador
    path('login/listar/editarJugador/', views.editarJugador) #ruta para el formulario de editar
]