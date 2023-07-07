from django.shortcuts import render, redirect, get_object_or_404
from .models import Eventos, Cliente, Carrito
from .forms import ContactanosForm, EventosForm, CustomUserCreationForm, CarritoForm, AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404 
from .forms import RegistroFormulario
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
# Resto del código de tus vistas...

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

#---USUARIOS---#    
def inicio_sesion(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['password']
        user = authenticate(request, username=correo, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Las credenciales de inicio de sesión son inválidas.'
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')

#------------Registro--------------------------------
def registro(request):
    if request.method == 'POST':
        formulario = RegistroFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Redirigir a la página de éxito
    else:
        formulario = RegistroFormulario()
    
    return render(request, 'registration/registro.html', {'formulario': formulario})

#-----------Fin Registro--------------------------------

#---PAGO---#    
def carrito_compras(request):
    eventos = Eventos.objects.all()
    """_summary_

    Returns:
        _type_: _description_
    
    if request.method == 'POST':
        form = CarritoForm(request.POST)
        if form.is_valid():
            evento_id = form.cleaned_data['evento_id']
            stock = form.cleaned_data['stock']

            # Obtener el objeto Evento según el evento_id
            Eventos = Eventos.objects.get(id=evento_id)

            # Agregar el evento al carrito
            # Aquí puedes realizar las acciones necesarias para el carrito de compras sin referenciar al campo 'usuario'

            messages.success(request, 'Entradas agregadas al carrito.')
            return redirect('carritocompras')
    else:
        form = CarritoForm()

    # Obtener los elementos del carrito del usuario actual
    # Aquí puedes realizar las acciones necesarias para mostrar los elementos del carrito sin referenciar al campo 'usuario'

    total_entradas = 0
    total = 0
    # Calcula el total de entradas y el precio total sin referenciar al campo 'usuario'

    context = {
        'form': form,
        'carrito': [],  # Puedes reemplazar esto con la lógica para obtener los elementos del carrito sin referenciar al campo 'usuario'
        'total_entradas': total_entradas,
        'total': total,
    }
    
    """

    return render(request, 'app/carrito.html',{"evento": eventos})

def resumenPedido(request):
    return render(request, 'app/resumenPedido.html')

def pago(request):
    return render(request, 'app/pago.html')

#------------Detalles Evento------------------------
def detalle_evento(request, evento_id):
    evento = get_object_or_404(Eventos, id=evento_id)
    
    context = {
        'evento': evento
    }
    
    return render(request, 'app/detalle_evento.html', context)

#------------Fin Detalles Evento------------------------

#----------------------ADMINISTRADOR----------------------------------

def homeAdmin(request):
    return render(request, 'app/admin/homeAdmin.html')

#---ADMIN-USUARIO---#
def gestionUsuarios(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/admin/gestionUsuarios.html', {"clientes": clientes})

def gestionUsuariosEditar(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/admin/gestionUsuariosEditar.html', {"clientes": clientes})

def registrarUsuario(request):
    nombre=request.POST['inputFirstName']
    apellido=request.POST['inputLastName']
    rut=request.POST['inputRut']
    correo=request.POST['inputEmail']
    contraseña=request.POST['typePassword']
    
    cliente=Cliente.objects.create(nombre=nombre, apellido=apellido, rut=rut, correo=correo, password=contraseña)
    
    return redirect('/gestionUsuarios')

def eliminarUsuario(request, rut):
    cliente = Cliente.objects.get(rut=rut)
    cliente.delete()
    
    return redirect('/gestionUsuarios')

def modificarUsuario(request, rut):
    cliente = Cliente.objects.get(rut=rut)
    
    return render(request, 'app/admin/gestionUsuariosEditar.html', {"cliente": cliente})

def editarUsuario(request):
    nombre=request.POST['inputFirstName']
    apellido=request.POST['inputLastName']
    rut=request.POST['inputRut']
    correo=request.POST['inputEmail']
    contraseña=request.POST['typePassword']
    
    cliente = Cliente.objects.get(rut=rut)
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.rut = rut
    cliente.correo = correo
    cliente.contraseña = contraseña
    
    cliente.save()
    
    return redirect('/gestionUsuarios')

#---ADMIN-EVENTO---#

def gestionEventos(request):
    eventos = Eventos.objects.all()
    return render(request, 'app/admin/gestionEventos.html', {"eventos": eventos})

def gestionEventosEditar(request):
    eventos = Eventos.objects.all()
    return render(request, 'app/admin/gestionEventosEditar.html', {"eventos": eventos})

def registrarEvento(request):
    id = request.POST['inputId']
    nombre = request.POST['inputNombre']
    categoria = request.POST['inputCategoria']
    fecha = request.POST['inputFecha']
    precio = request.POST['inputPrecio']
    stock = request.POST['inputStock']
    descripcion = request.POST['inputDescripcion']
    imagen = request.POST['inputImagen']
    
    evento = Eventos.objects.create(
        id=id,
        nombre=nombre,
        categoria=categoria,
        fecha=fecha,
        precio=precio,
        stock=stock,
        descripcion=descripcion,
        imagen=imagen,
    )
    
    return redirect('/gestionEventos')

def eliminarEvento(request, id):
    evento = Eventos.objects.get(id=id)
    evento.delete()
    
    return redirect('/gestionEventos')

def modificarEvento(request,id):
    evento = Eventos.objects.get(id=id)
    
    return render(request, 'app/admin/gestionEventosEditar.html', {"evento": evento})

def editarEvento(request):
    id = request.POST['inputId']
    nombre = request.POST['inputNombre']
    categoria = request.POST['inputCategoria']
    fecha = request.POST['inputFecha']
    precio = request.POST['inputPrecio']
    stock = request.POST['inputStock']
    descripcion = request.POST['inputDescripcion']
    imagen = request.POST['inputImagen']
    
    evento = Eventos.objects.get(id=id)
    
    evento.nombre = nombre
    evento.categoria = categoria
    evento.fecha = fecha
    evento.precio = precio
    evento.stock = stock
    evento.descripcion = descripcion
    evento.imagen = imagen
    
    evento.save()
    
    return redirect('/gestionEventos')
#---------------EVENTOS---------------#

def musica(request):
    eventos = Eventos.objects.filter(categoria='Musica')
    return render(request, 'app/home.html', {'eventos': eventos})

def deporte(request):
    eventos = Eventos.objects.filter(categoria='Deporte')
    return render(request, 'app/home.html', {'eventos': eventos})

def teatro(request):
    eventos = Eventos.objects.filter(categoria='Teatro')
    return render(request, 'app/home.html', {'eventos': eventos})

def familia(request):
    eventos = Eventos.objects.filter(categoria='Familia')
    return render(request, 'app/home.html', {'eventos': eventos})


#-----------Carrito de compras--------------------------
def agregar_al_carrito(request, evento_id):
    carrito = Carrito.objects.first()  # Obtener el carrito actual, puedes ajustar esta lógica según tus necesidades

    evento = Eventos.objects.get(id=evento_id)

    # Agregar lógica para agregar el evento al carrito aquí

    return JsonResponse({'message': 'Evento agregado al carrito'})

def carrito_compras(request):
    carrito = Carrito.objects.first()  # Obtener el carrito actual, puedes ajustar esta lógica según tus necesidades

    # Agregar lógica para obtener los elementos del carrito aquí

    total = 0  # Calcular el total del carrito aquí

    data = {
        'elementos_carrito': [],  # Puedes reemplazar esto con la lógica para obtener los elementos del carrito
        'total': total
    }

    return render(request, 'app/carrito.html', data)
     
