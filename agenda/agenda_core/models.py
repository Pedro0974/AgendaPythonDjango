from django.db import models


class Grupos(models.Model):
    nome = models.CharField(max_length=100)
    pessoa = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    lista_tarefas = models.ManyToManyField('Tarefa', related_name='agendas')

    def __str__(self):
        return f'Agenda #{self.id}'


class Tarefa(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    responsavel = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    cliente = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo