from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Empregador

class Empregador(LoginRequiredMixin, View):
    def get(self, request):
        data={}
        empregador  = Empregador.objects.all()
        return render(
            request, 'empregador/vagas_cadastradas.html',data)

class VagaCreate(LoginRequiredMixin, View):
    def get(self, request):
        data={}
        return  render(
            request, 'empregador/form.html')

    def post(self, request):
        user_logado = request.user.id
        empregador = Empregador.objects.create(
            nome_da_vaga = request.POST['nome_da_vaga'],
            faixa_salarial = request.POST['faixa_salarial'],
            escolaridade_minima = request.POST['escolaridade_minima'],
            autor = user_logado, usuarios_id = user_logado
            )

        #data['Empregador'] = Empregador
        #data['empregador']  = Empregador.objects.all().order_by('-id') 
        
        return render(request, 'empregador/form.html')
           