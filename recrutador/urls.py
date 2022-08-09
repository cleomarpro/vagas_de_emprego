from django.urls import  path
from recrutador import views
from .views import (VagasCadastradas, VagaCreate)
urlpatterns = [
    path('vagas_cadastradas/', VagasCadastradas.as_view(), name='vagas_cadastradas'),
    path('form/', VagaCreate.as_view(), name='criar_vaga'),
    
]