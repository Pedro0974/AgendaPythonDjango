from django.urls import path

from .views import (
    GruposListCreateView,
    GruposRetrieveUpdateDestroyView,
    TarefaListCreateView,
    TarefaRetrieveUpdateDestroyView,
    AgendaListCreateView,
    AgendaRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('grupos/', GruposListCreateView.as_view(), name='grupos-list'),
    path('grupos/<int:pk>/', GruposRetrieveUpdateDestroyView.as_view(), name='grupos-detail'),
    path('tarefas/', TarefaListCreateView.as_view(), name='tarefas-list'),
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyView.as_view(), name='tarefas-detail'),
    path('agenda/', AgendaListCreateView.as_view(), name='agenda-list'),
    path('agenda/<int:pk>/', AgendaRetrieveUpdateDestroyView.as_view(), name='agenda-detail'),
]