from django.shortcuts import render
from .models import Eventos
from .forms import ContactanosForm, EventosForm
# Create your views here.

#@login_required
def home(request):
    eventos_list = Eventos.objects.all()
    print(eventos_list)
    data = {
        'eventos': eventos_list
    }
    return render(request, 'app/home.html', data)

def contactanos(request):
    data = {
        'form': ContactanosForm()
    }
    
    if request.method == 'POST':
        formulario = ContactanosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje guardado"
        else:
            data["form"] = formulario
    return render(request, 'app/contactanos.html', data)

def soporte(request):
    return render(request, 'app/soporte.html')

def quienessomos(request):
        return render(request, 'app/quienessomos.html')

def registro(request):
        return render(request, 'app/registro.html')
    
def iniciosesion(request):
        return render(request, 'app/iniciosesion.html')
    
def agregar_eventos(request):
    
    data = {
        'form': EventosForm()
    }
    
    if request.method == 'POST':
        formulario = EventosForm(data=request.POST, files=request.FILES)
        if formulario.id.valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
        
    return render(request, 'app/eventos/agregar.html', data)

def listar_eventos(request):
    eventos = Eventos.objects.all()
    
    data = {
        'eventos': eventos
    }
    
    return render(request, 'app/eventos/listar.html', data)