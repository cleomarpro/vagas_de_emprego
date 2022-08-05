from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (MinhasVagas)

urlpatterns = [
    path('minhas_vagas/', MinhasVagas.as_view(), name='minhas_vagas')
]