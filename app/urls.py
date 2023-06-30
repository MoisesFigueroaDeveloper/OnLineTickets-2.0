from django.urls import path
from .views import contactanos, home, soporte, quienessomos, registro, login, agregar_eventos, listar_eventos, modificar_eventos, eliminar_eventos, homeAdmin, gestionEventos, gestionEventosEditar, gestionUsuarios, gestionUsuariosEditar
from .views import contactanos, home, soporte, quienessomos, registro, login, agregar_eventos, listar_eventos, modificar_eventos, eliminar_eventos, carrito_compras
from . import views

urlpatterns = [
    path('', home, name="home"),
    #---EVENTOS---#
    path('Eventos/musica/', views.musica, name="musica"),
    path('Eventos/deporte/', views.deporte, name="deporte"),
    path('Eventos/teatro', views.teatro, name="teatro"),
    path('Eventos/familia', views.familia , name="familia"),
    #---PAGO---#
    #---USUARIOS---#
    path('registration/registro/', registro, name="registro"),
    path('registration/login/', login, name="login"),
    
    path('contactanos/', contactanos, name="contactanos"),
    path('soporte/', soporte, name="soporte"),
    path('quienessomos/', quienessomos, name="quienessomos"),

    path('agregar-eventos/', agregar_eventos, name="agregar_eventos"),
    path('listar-eventos/', listar_eventos, name="listar_eventos"),
    path('modificar-eventos/<int:id>/', modificar_eventos, name="modificar_eventos"),
    path('eliminar-eventos/<int:id>/', eliminar_eventos, name="eliminar_eventos"),
    path('eventos/detalles/<int:evento_id>/', views.detalle_evento, name='evento_detalles'),
    path('carrito/', views.carrito_compras, name="carrito"),
    #---ADMIN---#
    path('homeAdmin/', homeAdmin, name="homeAdmin"),
    path('gestionEventos/', gestionEventos, name="gestionEventos"),
    path('gestionEventosEditar/', gestionEventosEditar, name="gestionEventosEditar"),
    path('gestionUsuarios/', gestionUsuarios, name="gestionUsuarios"),
    path('gestionUsuariosEditar/', gestionUsuariosEditar, name="gestionUsuariosEditar"),
    path('registrarUsuario/', views.registrarUsuario),
    path('eliminarUsuario/<rut>', views.eliminarUsuario),
    path('modificarUsuario/<rut>', views.modificarUsuario),
    path('editarUsuario/', views.editarUsuario),
    path('resumenPedido.html/', views.resumenPedido, name='resumenPedido'),
    path('pago.html/', views.pago, name='pago'),
]