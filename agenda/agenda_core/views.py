from rest_framework import generics
from .models import Agenda, Tarefa, Grupos
from .serializers import AgendaSerializer, TarefaSerializer, GruposSerializer


class GruposListCreateView(generics.ListCreateAPIView):
    queryset = Grupos.objects.all()
    serializer_class = GruposSerializer


class GruposRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grupos.objects.all()
    serializer_class = GruposSerializer


class TarefaListCreateView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


class TarefaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


class AgendaListCreateView(generics.ListCreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


class AgendaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer