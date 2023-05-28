from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contactanos(request):
    return render(request, 'app/contactanos.html')

def soporte(request):
    return render(request, 'app/soporte.html')

def quienessomos(request):
        return render(request, 'app/quienessomos.html')

def registro(request):
        return render(request, 'app/registro.html')
    
def iniciosesion(request):
        return render(request, 'app/iniciosesion.html')