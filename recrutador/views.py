from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vaga

class VagasCadastradas(LoginRequiredMixin, View):
    def get(self, request):
        data={}
        user_logado = request.user.id
        data['minhas_vagas'] = Vaga.objects.filter(autor = user_logado)
        return render(
            request, 'recrutador/vagas_cadastradas.html',data)

class VagaCreate(LoginRequiredMixin, View): 
    def get(self, request):
        return  render(
            request, 'recrutador/form.html')

    def post(self, request):

        user_logado = request.user.id
        recrutador = Vaga.objects.create(
            nome_da_vaga = request.POST['nome_da_vaga'],
            faixa_salarial = request.POST['faixa_salarial'],
            escolaridade_minima = request.POST['escolaridade_minima'],
            autor = user_logado 
            ) 
      
        return redirect('vagas_cadastradas')

class VagaUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        data = {}
        data['vaga'] = Vaga.objects.get(id = id) or None
        return  render(
            request, 'recrutador/form.html', data)

    def post(self, request, id):
        user_logado = request.user.id
        vaga = Vaga.objects.get(id = id) or None
        vaga.id = vaga.id 
        vaga.nome_da_vaga = request.POST['nome_da_vaga']
        vaga.faixa_salarial = request.POST['faixa_salarial']
        vaga.escolaridade_minima = request.POST['escolaridade_minima']
        vaga.autor = user_logado 
        vaga.save()
        return redirect('vagas_cadastradas')

def vaga_delete (request, id):
    vaga = Vaga.objects.get(id = id) or None
    if request.method == 'POST':
        vaga.delete()
        return redirect('vagas_cadastradas')
    else:
        return  render(
            request, 'recrutador/confirm_delete.html')