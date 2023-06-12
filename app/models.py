from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Eventos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="eventos", null=True)
    def __str__(self):
        return self.nombre
    
opciones_consultas = [
    [0, "consultas"],
    [1, "reclamos"],
    [2, "suguerencias"],
    [3, "Felicitaciones"]
]
    
class Contactanos(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_cosultas = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField(max_length=250)
    avisos = models.BooleanField()
    def __str__(self):
        return self.nombre