from django.urls import path
from .views import contactanos, home, soporte, quienessomos, registro, iniciosesion,carrito, adminHome, adminEntradas, adminUsuarios

urlpatterns = [
    path('', home, name="home"),
    path('contactanos/', contactanos, name="contactanos"),
    path('soporte/', soporte, name="soporte"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('registro/', registro, name="registro"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('iniciosesion/', carrito, name="carrito"),
    path('iniciosesion/', adminHome, name="admin"),
    path('iniciosesion/', adminUsuarios, name="adminUsuarios"),
    path('iniciosesion/', adminEntradas, name="adminEntradas"),

]
