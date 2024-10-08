from django.shortcuts import render, redirect
from .models import Jugador, User
# Create your views here.

# Crear vista para renderizar el archivo de inici en la ruta principal
def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, "iniciar_sesion.html")

# Vista para validar el formulario de login usando el modelo de users
def sesion(request):
    # Condicion para ver si se envio el formulario y tomar los valores enviados y guardarlos en la variables
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        # crear una variable donde se manda los datos guardados y devuelve un resultado la funcion que esta en models.py
        usuario_autenticado = User.verificar_credenciales(email, password)
        
        # condicion por si el usuario esta autenticado
        if usuario_autenticado:
        #    archivo que se dirige cuando se valida
            return redirect('/login/listar/')
        else:
            #retornar error y volver al  archivo de login para volver a validar 
            return render(request, 'iniciar_sesion.html', {'error': 'Credenciales incorrectas'})

    # Si no es una solicitud POST, simplemente renderiza el formulario
    return render(request, 'iniciar_sesion.html')


# funcion para renderizar el archivo para gestionar
def gestionar(request):
    return render(request, "gestion.html")

# funcion para renderizar la pagina inicial de lado admin
def listar(request):
    jugadorList = Jugador.objects.all() #traer listaa del modeels.py
    return render(request, "listar.html", {"jugadores": jugadorList}) #Enviar parametro al archivo


# Registar los datos del formulario gestion.html
def registrar(request):
    # Guardar los datos mandados desde formulario de Registrar Nuevo
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    numero = request.POST['txtNumero']
    
    # crear un nuevo jugador guardadando los valores que se mandaros de gestion.html
    jugadorNuevo = Jugador.objects.create(codigo=codigo, nombre=nombre, numero=numero)
    
    # redirigir a la ruta inical
    return redirect('http://127.0.0.1:8000/login/listar/')


# funcion para eliminar jugado
def eliminar(request, codigo): #se recibe parametro de listar.html con el id del jugador
    #coincidir resultados con el codigo enviado
    jugador= Jugador.objects.get(codigo=codigo) 
    jugador.delete() #funcion para eliminar el jugador
    
    return redirect('http://127.0.0.1:8000/login/listar/')

# funcion para mandar al archivo de editar.html los datos del jugador
def editar(request, codigo):
     jugador = Jugador.objects.get(codigo=codigo)
     return render(request,"editar.html",{"jugador":jugador}) #primer parametro, llamamos el objeto
 
 
#  funcion para realizar los cambios correctos del jugador
def editarJugador(request):
    # guardar los datos enviados en una variable
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    numero = request.POST['txtNumero']
    # coincidir el codigo mandado
    jugadorNuevo = Jugador.objects.get(codigo=codigo)
    # actualizar los campos del modelo con los enviados
    jugadorNuevo.nombre = nombre
    jugadorNuevo.numero = numero
    jugadorNuevo.save()
    return redirect('http://127.0.0.1:8000/login/listar/')