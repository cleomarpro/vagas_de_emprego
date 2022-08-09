from django.db import models
from django.utils import timezone
from recrutador.models import Vaga 

class Candidato(models.Model):
    pretecao_salarial = models.CharField(max_length=50, null=False)
    autor = models.CharField(max_length=100, null=False)
    data_hora = models.DateTimeField(default=timezone.now)
    vaga = models.ForeignKey(Vaga, null=False, on_delete=models.CASCADE)

class Experiencia (models.Model):
    nome_de_empresa = models.CharField(max_length=50, null=False)
    cargo = models.CharField(max_length=50, null=False)
    data_de_inicio = models.DateField(null=False)
    data_de_saida = models.DateField(null=True)
    obiservacao = models.CharField(max_length=200, blank=True)
    candidato = models.ForeignKey(Candidato, null=False, on_delete=models.CASCADE)

class Escolaridade (models.Model):
    instituicao = models.CharField(max_length=50, null=False)
    curso = models.CharField(max_length=50, null=False)
    data_de_inicio = models.DateField(blank=True, null=False)
    data_de_termino = models.DateField(blank=True, null=True)
    obiservacao = models.CharField(max_length=200, blank=True)
    candidato = models.ForeignKey(Candidato, null=False, on_delete=models.CASCADE)



