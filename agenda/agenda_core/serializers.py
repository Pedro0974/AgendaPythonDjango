from rest_framework import serializers
from .models import Agenda, Tarefa, Grupos


class GruposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupos
        fields = '__all__'


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'


class AgendaSerializer(serializers.ModelSerializer):
    lista_tarefas = TarefaSerializer(many=True)

    class Meta:
        model = Agenda
        fields = '__all__'

    def create(self, validated_data):
        tarefas_data = validated_data.pop('lista_tarefas')
        agenda = Agenda.objects.create(**validated_data)

        for tarefa_data in tarefas_data:
            Tarefa.objects.create(agenda=agenda, **tarefa_data)

        return agenda