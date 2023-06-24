from django import forms
from django.db import models
from .models import Contactanos, Eventos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .models import Cliente


class ContactanosForm(forms.ModelForm):
    
    class Meta:
        model = Contactanos
        #fields = ["nombre", "correo", "tipo_consultas", "mensaje", "avisos"]
        fields = '__all__'
        
class EventosForm(forms.ModelForm):
    
    class Meta:
        model = Eventos
        fields = '__all__'
        
class RegistroFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'rut', 'correo', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
        
class InicioSesionForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['correo', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


        
class CustomUserCreationForm(UserCreationForm):
    pass 


