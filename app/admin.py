from django.contrib import admin
from .models import Cliente, Eventos, Contactanos

class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "correo"]
    search_fields = ["nombre"]
    list_per_page = 12

class EventosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "descripcion", "precio"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["categoria"]
    list_per_page = 12
    

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Eventos, EventosAdmin)
admin.site.register(Contactanos, ContactanosAdmin)
