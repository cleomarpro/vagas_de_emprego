from django.urls import  path
from recrutador import views
from .views import (
    VagasCadastradas, 
    VagaUpdate,
    VagaCreate,
    Candidato,
    Curriculo
 )
urlpatterns = [
    path('vagas_cadastradas/', VagasCadastradas.as_view(), name='vagas_cadastradas'),
    path('candidatos/<int:id>/', Candidato.as_view(), name='candidatos'),
    path('curriculo/<int:id>/', Curriculo.as_view(), name='curriculo'),
    path('form/', VagaCreate.as_view(), name='criar_vaga'),
    path('form/<int:id>/', VagaUpdate.as_view(), name='vaga_updade'),
    path('confirm_delete/(?P<id>\d+)/', views.vaga_delete, name='confirm_delete'),
    
]