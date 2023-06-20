from django.urls import path
from .views import contactanos, home, soporte, quienessomos, registro, iniciosesion,carrito, adminHome, adminEntradas, adminUsuarios

urlpatterns = [
    path('', home, name="home"),
    path('contactanos/', contactanos, name="contactanos"),
    path('soporte/', soporte, name="soporte"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('registro/', registro, name="registro"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('carrito/', carrito, name="carrito"),
    path('adminhome/', adminHome, name="admin"),
    path('adminUsuarios/', adminUsuarios, name="adminUsuarios"),
    path('adminEntradas/', adminEntradas, name="adminEntradas"),

]
