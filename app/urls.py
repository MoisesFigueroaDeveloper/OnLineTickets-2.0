from django.urls import path
from .views import contactanos, home, soporte, quienessomos, registro, iniciosesion

urlpatterns = [
    path('', home, name="home"),
    path('contactanos/', contactanos, name="contactanos"),
    path('soporte/', soporte, name="soporte"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('registro/', registro, name="registro"),
    path('iniciosesion/', iniciosesion, name="iniciosesion")
]
