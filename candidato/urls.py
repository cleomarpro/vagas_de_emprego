from django.urls import path
from candidato import views
from django.contrib.auth import views as auth_views
from .views import (
    MinhasVagas,
    EscolaridadeCreate, 
    ExperienciaCreate,
    MinhaIscricaoCreate,
    Curriculo,
    DetalhesVaga,
    DadosPessoaisUpdate,
    EscolaridadeUpdate,
    ExperienciaUpdate,
    PretencaoSalarialUpdate
)

urlpatterns = [
    path('iscricao_confirm_delete/(?P<id>\d+)/', views.iscricao_delete, name='iscricao_confirm_delete'),
    path('detalhes_da_vaga/<int:id>/', DetalhesVaga.as_view(), name='detalhes_da_vaga'),
    path('curriculo/', Curriculo.as_view(), name='curriculo'),
    path('minhas_vagas/', MinhasVagas.as_view(), name='minhas_vagas'),
    path('escolaridade/<int:id>/', EscolaridadeUpdate.as_view(), name='escolaridade_update'),
    path('escolaridade/', EscolaridadeCreate.as_view(), name='escolaridade_create'),
    path('escolaridade_confirm_delete/(?P<id>\d+)/', views.escolaridade_delete, name='escolaridade_confirm_delete'),
    path('experiencia/', ExperienciaCreate.as_view(), name='experiencia_create'),
    path('experiencia/<int:id>/', ExperienciaUpdate.as_view(), name='experiencia_update'),
    path('experiencia_confirm_delete/(?P<id>\d+)/', views.experiencia_delete, name='experiencia_confirm_delete'),
    path('candidato/<int:id>/', MinhaIscricaoCreate.as_view(), name='candidato'),
    path('pretencao_salarial/', PretencaoSalarialUpdate.as_view(), name='pretencao_salarial'),
    path('dados_pessoais/<int:id>/', DadosPessoaisUpdate.as_view(), name='dados_pessoais')
]