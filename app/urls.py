from django.urls import path
from .views import contactanos, home, soporte, quienessomos, registro, iniciosesion, agregar_eventos, listar_eventos

urlpatterns = [
    path('', home, name="home"),
    path('contactanos/', contactanos, name="contactanos"),
    path('soporte/', soporte, name="soporte"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('registro/', registro, name="registro"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('agregar-eventos/', agregar_eventos, name="agregar_eventos"),
    path('listar-eventos/', listar_eventos, name="listar_eventos"),
]
