from django.db import models

# Create your models here.


# Modelo para registro de usuarios
class Registro(models.Model):
    nombre = models.TextField(max_length=50, verbose_name='Nombre de usuario')
    correo = models.EmailField(max_length=50, verbose_name= 'Correo')
    contraseña = models.TextField(max_length=50, verbose_name= 'Contraseña')

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, verbose_name= 'Apellidos')
    rut = models.TextField(max_length=50, verbose_name= 'Rut')
    telefono = models.TextField(max_length=50, verbose_name= 'Telefono')
    correo = models.EmailField(max_length=50, verbose_name= 'Correo')
    comentario = models.CharField(max_length=50, verbose_name= 'Comentarios')

    def __str__(self):
        return self.nombres