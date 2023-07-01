import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

rut_regex = r'^\d{7,8}-[0-9kK]{1}$'
rut_validator = RegexValidator(rut_regex, 'El RUT debe tener el siguiente formato: 19999999-9 o 9999999-9 o 19999999-K.')

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True, validators=[rut_validator], default='00000000-0')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} {1}"
        return texto(self.nombre, self.apellido)

    
class Eventos(models.Model):
    EVENTOS = (
        (0, 'Musica'),
        (1, 'Deporte'),
        (2, 'Teatro'),
        (3, 'Familia'),
    )
    id = models.CharField(max_length=6, unique=True, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=10)
    fecha = models.DateField(blank=True, null=True)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
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
    tipo_consultas = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField(max_length=250)
    avisos = models.BooleanField()
    def __str__(self):
        return self.nombre
    
