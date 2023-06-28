from django.urls import path
from .views import contactanos, home, soporte, quienessomos, registro, login, agregar_eventos, listar_eventos, modificar_eventos, eliminar_eventos, homeAdmin, gestionEventos, gestionEventosEditar, gestionUsuarios, gestionUsuariosEditar
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('contactanos/', contactanos, name="contactanos"),
    path('soporte/', soporte, name="soporte"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('registro/', registro, name="registro"),
    path('login/', login, name="login"),
    path('agregar-eventos/', agregar_eventos, name="agregar_eventos"),
    path('listar-eventos/', listar_eventos, name="listar_eventos"),
    path('modificar-eventos/<int:id>/', modificar_eventos, name="modificar_eventos"),
    path('eliminar-eventos/<int:id>/', eliminar_eventos, name="eliminar_eventos"),
    path('eventos/detalles/<int:evento_id>/', views.detalle_evento, name='evento_detalles'),
    
    path('homeAdmin/', homeAdmin, name="homeAdmin"),
    path('gestionEventos/', gestionEventos, name="gestionEventos"),
    path('gestionEventosEditar/', gestionEventosEditar, name="gestionEventosEditar"),
    path('gestionUsuarios/', gestionUsuarios, name="gestionUsuarios"),
    path('gestionUsuariosEditar/', gestionUsuariosEditar, name="gestionUsuariosEditar"),
    path('registrarUsuario/', views.registrarUsuario),
]