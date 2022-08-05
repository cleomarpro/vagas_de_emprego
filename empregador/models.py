from django.db import models
from django.utils import timezone

class Empregador (models.Model):
    nome_da_vaga = models.CharField(max_length=50, blank=True)
    faixa_salarial = models.CharField(max_length=50, blank=True)
    escolaridade_minima = models.CharField(max_length=50, blank=True)
    autor = models.CharField(max_length=100, blank=True, null=True)
    data_hora = models.DateTimeField(default=timezone.now)

    def __str__(self): # METODO CONSTRUTOR
       return self.nome_da_vaga

