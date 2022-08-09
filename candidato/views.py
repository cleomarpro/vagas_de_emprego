from django.shortcuts import render, redirect
from django.views import View
from .models import Vaga
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from candidato.models import Candidato, Experiencia, Escolaridade

class Curriculo(View):
    def get(self, request, id):
        data = {}
        data['candidato'] = Candidato.objects.get(id = id)
        data['escolaridade'] = Escolaridade.objects.filter(candidato_id = id)
        data['experiencia'] = Experiencia.objects.filter(candidato_id = id)
        return render(
            request, 'candidato/curriculo.html', data)

class MinhasVagas(View):
    def get(self, request):
        data = {}
        user_logado = request.user.id
        data['minhas_vagas'] = Candidato.objects.filter(autor = user_logado)
        return render(
            request, 'candidato/minhas_vagas.html', data)

class DetalhesVaga(View):
    def get(self, request, id):
        data = {}
        data['candidato'] = Candidato.objects.get(id = id)
        return render(
            request, 'candidato/detalhes_da_vaga.html', data)

class Vagas(LoginRequiredMixin, View):
    def get(self, request):
        data = {}
        vagas = Vaga.objects.all()
        return render(
            request, 'candidato/minhas_vagas.html')

class CandidatoCreate(LoginRequiredMixin, View):
    def get(self, request, id):
        data = {}
        
        return render(
            request, 'candidato/candidato.html')

    def post(self, request, id):
        user_logado = request.user.id
        candidato = Candidato.objects.create(
            pretecao_salarial = request.POST['pretecao_salarial'],
            vaga_id = id,
            autor = user_logado
            )
        return redirect('escolaridade', id = candidato.id)

class EscolaridadeCreate(View):
    def get(self, request, id):
        data = {}
        
        return render(
            request, 'candidato/escolaridade.html')

    def post(self, request, id):
        inicio = request.POST['inicio']
        inicio =  datetime.datetime.strptime(inicio, "%Y-%m-%d")

        data_de_termino = request.POST['data_de_termino']
        data_de_termino =  datetime.datetime.strptime(data_de_termino, "%Y-%m-%d")

        escolaridade = Escolaridade.objects.create(
            instituicao = request.POST['instituicao'],
            curso = request.POST['curso'],
            data_de_inicio = inicio,
            data_de_termino = data_de_termino,
            obiservacao = request.POST['obiservacao'],
            candidato_id = id
            )
        
        return redirect('experiencia', id = id)

class ExperienciaCreate(View):
    def get(self, request, id):
        data = {}
       
        return render(
            request, 'candidato/experiencia.html')
    def post(self, request, id):
        data_de_saida = request.POST['data_de_saida']
        data_de_saida =  datetime.datetime.strptime(data_de_saida, "%Y-%m-%d")

        data_de_inicio = request.POST['data_de_inicio']
        data_de_inicio =  datetime.datetime.strptime(data_de_inicio, "%Y-%m-%d")

        experiencia = Experiencia.objects.create(
            nome_de_empresa = request.POST['nome_de_empresa'],
            cargo = request.POST['cargo'],
            data_de_inicio = data_de_inicio, 
            data_de_saida = data_de_saida,
            obiservacao = request.POST['obiservacao'],
            candidato_id = id
            )
        
        return redirect('detalhes_da_vaga', id =id)