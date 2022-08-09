from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    MinhasVagas,
    EscolaridadeCreate, 
    ExperienciaCreate,
    CandidatoCreate,
    Curriculo
)

urlpatterns = [
    path('curriculo/<int:id>/', Curriculo.as_view(), name='curriculo'),
    path('minhas_vagas/', MinhasVagas.as_view(), name='minhas_vagas'),
    path('escolaridade/<int:id>/', EscolaridadeCreate.as_view(), name='escolaridade'),
    path('experiencia/<int:id>/', ExperienciaCreate.as_view(), name='experiencia'),
    path('candidato/<int:id>/', CandidatoCreate.as_view(), name='candidato')
]