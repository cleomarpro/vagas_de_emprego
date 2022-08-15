from django.db import models
from django.utils import timezone
from recrutador.models import Vaga 
from django.contrib.auth.models import User

class DadosPessoais (models.Model):
    nome = models.CharField(max_length=50, null=False)
    segundo_nome = models.CharField(max_length=50, null=False)
    telefone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=False)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

class MinhaIscricao(models.Model):
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(default=timezone.now)
    vaga = models.ForeignKey(Vaga, null=False, on_delete=models.CASCADE)
    dados_pessoais = models.ForeignKey(DadosPessoais, null=False, on_delete=models.CASCADE)

class VagaIscricao (models.Model):
    vaga = models.ForeignKey(Vaga, null=False, on_delete=models.CASCADE)
    iscricao = models.ForeignKey(MinhaIscricao, null=False, on_delete=models.CASCADE)

class Experiencia (models.Model):
    nome_da_empresa = models.CharField(max_length=50, null=False)
    cargo = models.CharField(max_length=50, null=False)
    data_de_inicio = models.DateField(null=False)
    data_de_saida = models.DateField(null=True)
    obiservacao = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

class Escolaridade (models.Model):
    instituicao = models.CharField(max_length=50, null=False)
    curso = models.CharField(max_length=50, null=False)
    data_de_inicio = models.DateField(blank=True, null=False)
    data_de_termino = models.DateField(blank=True, null=True)
    obiservacao = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    
class PretencaoSalarial (models.Model):
    pretencao_salarial = models.CharField(max_length=50, null=False)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

