from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class eventos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="eventos", null=True)
    def __str__(self):
        return self.nombre