from django.shortcuts import render, redirect
from django.views import View
from .models import Vaga
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from candidato.models import*

class Curriculo(View):
    def get(self, request):
        data = {}
        user_logado = request.user.id
        data['pretencao_salarial'] = PretencaoSalarial.objects.get(owner = user_logado)
        data['dados_pessoais'] = DadosPessoais.objects.get(owner = user_logado)
        data['escolaridade'] = Escolaridade.objects.filter(owner = user_logado)
        data['experiencia'] = Experiencia.objects.filter(owner = user_logado)
        return render(
            request, 'candidato/curriculo.html', data)

class MinhasVagas(View):
    def get(self, request):
        data = {}
        data['minhas_vagas'] = MinhaIscricao.objects.filter(owner = request.user.id)
        return render(
            request, 'candidato/minhas_vagas.html', data)

class DetalhesVaga(View):
    def get(self, request, id):
        data = {}
        data['dados_pessoais'] = DadosPessoais.objects.get(owner = request.user.id)
        data['iscricao'] = MinhaIscricao.objects.get(id = id)
        return render(
            request, 'candidato/detalhes_da_vaga.html', data)

class Vagas(LoginRequiredMixin, View):
    def get(self, request):
        data = {}
        vagas = Vaga.objects.all()
        return render(
            request, 'candidato/minhas_vagas.html')

class MinhaIscricaoCreate(LoginRequiredMixin, View):
    def get(self, request, id):
        iscricao = MinhaIscricao.objects.filter(vaga_id=id)
        if iscricao:
            return redirect('vagas')
        else:
            user_logado = request.user.id
            iscricao = MinhaIscricao.objects.create(
                vaga_id = id,
                owner = user_logado
                )
            return redirect('detalhes_da_vaga', id = iscricao.id)

def iscricao_delete (request, id):
    iscricao = MinhaIscricao.objects.filter(id = id) or None
    if request.method == 'POST':
        iscricao.delete()
        return redirect('minhas_vagas')
    else:
        return  render(
            request, 'candidato/confirm_delete.html')

class EscolaridadeCreate(View):
    def get(self, request):    
        return render(
            request, 'candidato/escolaridade.html')

    def post(self, request):
        user_logado = request.user.id

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
            owner = user_logado
            )
        return redirect('curriculo')


class EscolaridadeUpdate(View):
    def get(self, request, id):
        data = {}
        data['escolaridade'] = Escolaridade.objects.get(id = id)
        return render(
            request, 'candidato/escolaridade.html', data)

    def post(self, request, id):
        user_logado = request.user.id

        inicio = request.POST['inicio']
        inicio =  datetime.datetime.strptime(inicio, "%Y-%m-%d")

        data_de_termino = request.POST['data_de_termino']
        data_de_termino =  datetime.datetime.strptime(data_de_termino, "%Y-%m-%d")

        escolaridade = Escolaridade.objects.get(id = id)
        escolaridade.instituicao = request.POST['instituicao']
        escolaridade.curso = request.POST['curso']
        escolaridade.data_de_inicio = inicio
        escolaridade.data_de_termino = data_de_termino
        escolaridade.obiservacao = request.POST['obiservacao']
        escolaridade.save()
        return redirect('curriculo')

def escolaridade_delete (request, id):
    escolaridade = Escolaridade.objects.get(id = id) or None
    if request.method == 'POST':
        escolaridade.delete()
        return redirect('curriculo')
    else:
        return  render(
            request, 'candidato/confirm_delete.html')

class ExperienciaCreate(View):
    def get(self, request):
        return render(
            request, 'candidato/experiencia.html')
    def post(self, request):
        user_logado = request.user.id

        data_de_saida = request.POST['data_de_saida']
        data_de_saida =  datetime.datetime.strptime(data_de_saida, "%Y-%m-%d")

        data_de_inicio = request.POST['data_de_inicio']
        data_de_inicio =  datetime.datetime.strptime(data_de_inicio, "%Y-%m-%d")

        experiencia = Experiencia.objects.create(
            nome_da_empresa = request.POST['nome_da_empresa'],
            cargo = request.POST['cargo'],
            data_de_inicio = data_de_inicio, 
            data_de_saida = data_de_saida,
            obiservacao = request.POST['obiservacao'],
            owner = user_logado
            )
        return redirect('curriculo')

class ExperienciaUpdate(View):
    def get(self, request, id):
        data = {}
        data['experiencia'] = Experiencia.objects.get(id = id)
        return render(
            request, 'candidato/experiencia.html', data)
    def post(self, request, id):
        user_logado = request.user.id

        data_de_saida = request.POST['data_de_saida']
        data_de_saida =  datetime.datetime.strptime(data_de_saida, "%Y-%m-%d")

        data_de_inicio = request.POST['data_de_inicio']
        data_de_inicio =  datetime.datetime.strptime(data_de_inicio, "%Y-%m-%d")

        experiencia = Experiencia.objects.get(id = id)
        experiencia.nome_da_empresa = request.POST['nome_da_empresa']
        experiencia.cargo = request.POST['cargo']
        experiencia.data_de_inicio = data_de_inicio
        experiencia.data_de_saida = data_de_saida
        experiencia.obiservacao = request.POST['obiservacao']
        experiencia.save()
        return redirect('curriculo')

def experiencia_delete (request, id):
    experiencia = Experiencia.objects.get(id = id) or None
    if request.method == 'POST':
        experiencia.delete()
        return redirect('curriculo')
    else:
        return  render(
            request, 'candidato/confirm_delete.html')

class PretencaoSalarialUpdate(View):
    def get(self, request):
        return render(
            request, 'candidato/pretencao_salarial.html')
    def post(self, request):
        user_logado = request.user.id
        pretencao_salarial_id = PretencaoSalarial.objects.get(owner = user_logado)
        pretencao_salarial_id = pretencao_salarial_id.id
        if pretencao_salarial_id:
            pretencao_salarial = PretencaoSalarial.objects.get(id = pretencao_salarial_id)
            pretencao_salarial.id = pretencao_salarial_id
            pretencao_salarial.pretencao_salarial = request.POST['pretencao_salarial']
            pretencao_salarial.owner = user_logado
            pretencao_salarial.save()
        else:
            pretencao_salarial = PretencaoSalarial.objects.create(
                pretencao_salarial = request.POST['pretencao_salarial'],
                owner = user_logado
            )
        return redirect('curriculo')

class DadosPessoaisUpdate(View):
    def get(self, request, id):
        data = {}
        data['dados_pessoais'] = DadosPessoais.objects.get(id=id)
        return render(
            request, 'candidato/dados_pessoais.html', data)
    def post(self, request, id):
        dados_pessoais = DadosPessoais.objects.get(id=id)
        dados_pessoais.nome = request.POST['nome']
        dados_pessoais.segundo_nome = request.POST['segundo_nome']
        dados_pessoais.telefone = request.POST['telefone']
        dados_pessoais.email = request.POST['email']
        dados_pessoais.save()
        return redirect('curriculo')
