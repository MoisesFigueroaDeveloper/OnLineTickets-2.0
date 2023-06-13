from django import forms
from .models import Contactanos, Eventos

class ContactanosForm(forms.ModelForm):
    
    class Meta:
        model = Contactanos
        #fields = ["nombre", "correo", "tipo_consultas", "mensaje", "avisos"]
        fields = '__all__'
        
class EventosForm(forms.ModelForm):
    
    class Meta:
        model = Eventos
        fields = '__all__'
        
        