from django.contrib import admin
from .models import Agenda, Tarefa, Grupos


class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'horario', 'titulo', 'descricao')


admin.site.register(Tarefa)
admin.site.register(Grupos)