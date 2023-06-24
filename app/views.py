from django.shortcuts import render, redirect, get_object_or_404
from .models import Eventos
from .forms import ContactanosForm, EventosForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404 
from .forms import RegistroFormulario
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# Create your views here.

#@login_required
def home(request):
    eventos_list = Eventos.objects.all()
    print(eventos_list)
    data = {
        'eventos': eventos_list
    }
    return render(request, 'app/home.html', data)

#-----------Formulario Contactanos-----------
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

    
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a la página de inicio o a la página deseada después de iniciar sesión
            return redirect('home')  # Reemplaza 'home' con la URL de la página deseada
        else:
            # Mostrar un mensaje de error indicando que las credenciales son inválidas
            error_message = 'Las credenciales de inicio de sesión son inválidas.'
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')
    
    
#-----------------------CRUD------------------------

#-----------Agregar Eventos-----------
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

#-----------Listar Eventos-----------
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

#-----------Modificar Eventos-----------
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

#-----------Eliminar Eventos-----------
def eliminar_eventos(request, id):
    eventos = get_object_or_404(Eventos, id=id)
    eventos.delete()
    return redirect(to="listar_eventos")

#-----------------------FIN CRUD------------------------

#------------Formulario Registro------------------------
def registro(request):
    if request.method == 'POST':
        formulario = RegistroFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Redirigir a la página de éxito
    else:
        formulario = RegistroFormulario()
    
    return render(request, 'registration/registro.html', {'formulario': formulario})


#-----------------------FIN Formulario Registro------------------------

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Eventos, id=evento_id)
    
    context = {
        'evento': evento
    }
    
    return render(request, 'app/detalle_evento.html', context)
