from django.urls import path
from .views import contactanos, home, soporte, quienessomos, registro, login, homeAdmin, gestionEventos, gestionEventosEditar, gestionUsuarios, gestionUsuariosEditar
from . import views

urlpatterns = [
    path('', home, name="home"),
    #---EVENTOS---#
    path('', views.home, name='home'),
    path('musica/', views.musica, name='musica'),
    path('deporte/', views.deporte, name='deporte'),
    path('teatro/', views.teatro, name='teatro'),
    path('familia/', views.familia, name='familia'),
    #---PAGO---#
    #---USUARIOS---#
    path('registration/registro/', registro, name="registro"),
    path('registration/login/', login, name="login"),
    
    path('contactanos/', contactanos, name="contactanos"),
    path('soporte/', soporte, name="soporte"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('eventos/detalles/<int:evento_id>/', views.detalle_evento, name='evento_detalles'),
    path('carrito/', views.carrito_compras, name="carrito"),
    path('resumenPedido.html/', views.resumenPedido, name='resumenPedido'),
    path('pago/', views.pago, name='pago'),
    #---ADMIN---#
    path('homeAdmin/', homeAdmin, name="homeAdmin"),
    
    path('gestionUsuarios/', gestionUsuarios, name="gestionUsuarios"),
    path('gestionUsuariosEditar/', gestionUsuariosEditar, name="gestionUsuariosEditar"),
    path('registrarUsuario/', views.registrarUsuario),
    path('eliminarUsuario/<rut>', views.eliminarUsuario),
    path('modificarUsuario/<rut>', views.modificarUsuario),
    path('editarUsuario/', views.editarUsuario),
    
    path('gestionEventos/', gestionEventos, name="gestionEventos"),
    path('gestionEventosEditar/', gestionEventosEditar, name="gestionEventosEditar"),
    path('registrarEvento/', views.registrarEvento),
    path('eliminarEvento/<id>', views.eliminarEvento),
    path('modificarEvento/<id>', views.modificarEvento),
    path('editarEvento/', views.editarEvento)
]