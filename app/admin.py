from django.contrib import admin
from app.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo',)

admin.site.register(Evento, EventoAdmin)