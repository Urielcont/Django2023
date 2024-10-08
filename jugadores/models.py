from django.db import models

# Create your models here.

# Crear nuestro modelo con el campo de nuestra bd para tabla jugador
class Jugador(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    numero=models.CharField(max_length=3) #se usa para datos pequeños, enteros, positivos
    
    # Retornar el texto de un objeto de forma normal
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.codigo, self.nombre, self.numero)
    
# tabla para usuarios   
class User(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    correo=models.CharField(max_length=50)
    password=models.CharField(max_length=3)
    
    # especificar que ees  @classmethod
    @classmethod
    # funcion para validar el registro que se guarda en una variable de views.py
    def verificar_credenciales(cls, correo, password):
        try:
            usuario = cls.objects.get(correo=correo, password=password)
            return usuario
        except cls.DoesNotExist:
            return None