from django.urls import  path
from empregador import views
from .views import (Empregador, EmpregadorCreate)
urlpatterns = [
    path('', Empregador.as_view(), name='vagas_cadastradas'),
    path('form/', EmpregadorCreate.as_view(), name='criar_vaga'),
    
]