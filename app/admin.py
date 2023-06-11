from django.contrib import admin
from .models import cliente, eventos

class EventosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "descripcion", "precio"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["categoria"]
    list_per_page = 12

# Register your models here.
admin.site.register(cliente)
admin.site.register(eventos, EventosAdmin)
