from django.db import models
from django.utils import timezone

class Vaga (models.Model):
    nome_da_vaga = models.CharField(max_length=50, null=False)
    faixa_salarial = models.CharField(max_length=50, null=False)
    escolaridade_minima = models.CharField(max_length=50, null=False)
    autor = models.CharField(max_length=100, null=False)
    data_hora = models.DateTimeField(default=timezone.now)

    def __str__(self): # METODO CONSTRUTOR
       return self.nome_da_vaga

