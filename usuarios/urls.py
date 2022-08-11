from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    CandidatoUserCreate,
    RecrutadorUseCreate
)
  
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('candidato/', CandidatoUserCreate.as_view(), name='candidato_novo'),
    path('recrutador/', RecrutadorUseCreate.as_view(), name='recrutador_novo'),
]