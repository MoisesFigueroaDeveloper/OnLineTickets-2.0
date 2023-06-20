from django.shortcuts import render
from .models import Eventos
from .forms import ContactanosForm
# Create your views here.

def home(request):
    eventos_list = Eventos.objects.all()
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

def carrito(request):
        return render(request, 'app/carrito.html')
    
def adminHome(request):
        return render(request, 'app/adminHome.html')
    
def adminUsuarios(request):
        return render(request, 'app/adminUsuarios.html')
    
def adminEntradas(request):
        return render(request, 'app/adminEntradas.html')