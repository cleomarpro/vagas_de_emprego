from django.urls import  path
from empregador import views
from .views import (VagasCadastradas, VagaCreate)
urlpatterns = [
    path('', VagasCadastradas.as_view(), name='vagas_cadastradas'),
    path('form/', VagaCreate.as_view(), name='criar_vaga'),
    
]