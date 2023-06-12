from django import forms
from .models import Contactanos

class ContactanosForm(forms.ModelForm):
    
    class Meta:
        model = Contactanos
        #fields = ["nombre", "correo", "tipo_consultas", "mensaje", "avisos"]
        fields = '__all__'