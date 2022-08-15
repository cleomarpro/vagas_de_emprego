from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Vaga (models.Model):
    nome_da_vaga = models.CharField(max_length=50, null=False)
    faixa_salarial = models.CharField(max_length=50, null=False)
    escolaridade_minima = models.CharField(max_length=50, null=False)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(default=timezone.now)

    def __str__(self): # METODO CONSTRUTOR
       return self.nome_da_vaga

