from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class Empregador(LoginRequiredMixin, View):
    def get(self, request):
        
        return render(
            request, 'Empregador/vagas_cadastradas.html')

class EmpregadorCreate(LoginRequiredMixin, View):
    def get(self, request):
           
            return render(
                request, 'Empregador/form.html')