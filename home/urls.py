from django.urls import  path
from home import views
from .views import (Vagas)

urlpatterns = [
    path('', views.home, name='home'),
    path('vagas/', Vagas.as_view(), name='vagas'),
]
