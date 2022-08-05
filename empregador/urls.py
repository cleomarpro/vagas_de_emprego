from django.urls import  path
from empregador import views
from .views import (Empregador, VagaCreate)
urlpatterns = [
    path('', Empregador.as_view(), name='vagas_cadastradas'),
    path('form/', VagaCreate.as_view(), name='criar_vaga'),
    
]