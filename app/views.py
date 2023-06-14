from django.shortcuts import render, redirect, get_object_or_404
from .models import Eventos
from .forms import ContactanosForm, EventosForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404 
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
    page = request.GET.get('page', 1)
    
    try: 
        paginator = Paginator(eventos, 5)
        eventos = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'eventos': eventos
    }
    
    return render(request, 'app/eventos/listar.html', data)

def modificar_eventos(request, id):
    eventos = get_object_or_404(Eventos, id= id)
    
    data = {
        'form': EventosForm(instance=eventos)
    }
    
    if request.method == 'POST':
        formulario = EventosForm(data=request.POST, instance=eventos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificacion exitosa")
            return redirect(to="listar_eventos")
        data["form"] = formulario
        
    return render(request, 'app/eventos/modificar.html', data)

def eliminar_eventos(request, id):
    eventos = get_object_or_404(Eventos, id=id)
    eventos.delete()
    return redirect(to="listar_eventos")
