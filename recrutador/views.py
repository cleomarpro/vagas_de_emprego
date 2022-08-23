from django.shortcuts import render, redirect
from django.views import View
from django.db.models.aggregates import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Vaga
from django.conf import settings
from candidato.models import*

class Candidato(View):
    def get(self, request, id):
        user = request.user.has_perm('recrutador.view_vaga')
        if user == False:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        data={}
        candidatos = MinhaIscricao.objects.filter(vaga_id = id)
        candidato = MinhaIscricao.objects.all().values('id',
            'pretencao_salarial__pretencao_salarial','vaga__faixa_salarial')
        candidato= list(candidato)
        pontuacao = 3
        a = 'Até 1000'
        b = '1000 a 2000'
        c = '2000 a 3000'
        d = 'Acima de 3000'
        for pontuacao_candidato in candidato:
            pretencao_salarial = pontuacao_candidato['pretencao_salarial__pretencao_salarial']
            faixa_salaria = pontuacao_candidato['vaga__faixa_salarial']
            
            
            if  faixa_salaria == a:
                pontuacao = float(pretencao_salarial) <= 1000
                if pontuacao == True:
                    pontuacao = 1
                else:
                    pontuacao = 0
            elif faixa_salaria == b:
                pontuacao = float(pretencao_salarial) >= 1000 and  float(pretencao_salarial) <= 2000
                if pontuacao == True:
                    pontuacao = 1
                else:
                    pontuacao = 0
                   
            elif faixa_salaria == c:
                pontuacao = float(pretencao_salarial) >= 2000 and  float(pretencao_salarial) <= 3000
                if pontuacao == True:
                    pontuacao = 1
                else:
                    pontuacao = 0
                  
            elif faixa_salaria == c:
                pontuacao = float(pretencao_salarial) > 3000
                if pontuacao == True:
                    pontuacao = 1
                else:
                    pontuacao = 0
                
            data['pontuacao'] = pontuacao
            data['candidatos'] = candidatos
            return render(
                request, 'recrutador/candidatos.html',data)
            
class VagasCadastradas(View):
    def get(self, request):
        user = request.user.has_perm('recrutador.view_vaga')
        if user == False:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        data={}
        user_logado = request.user.id
        total_candidatos = Vaga.objects.filter(owner_id = user_logado).annotate(
            count = Count('minhaiscricao')).values(
                'count','nome_da_vaga','escolaridade_minima','faixa_salarial','data_hora','id')
        data['total_candidatos'] = total_candidatos
        data['minhas_vagas'] = Vaga.objects.filter(owner_id = user_logado)
        return render(
            request, 'recrutador/vagas_cadastradas.html',data)
            
class Curriculo(View):
    def get(self, request, id):
        user = request.user.has_perm('recrutador.view_vaga')
        if user == False:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        data={}
        if PretencaoSalarial.objects.filter(owner_id = id):
            data['pretencao_salarial'] = PretencaoSalarial.objects.get(owner_id = id)
        data['dados_pessoais'] = DadosPessoais.objects.get(owner_id = id)
        data['escolaridade'] = Escolaridade.objects.filter(owner_id = id)
        data['experiencia'] = Experiencia.objects.filter(owner_id = id)
        return render(
            request, 'recrutador/curriculo.html',data)

class VagaCreate( View): 
    def get(self, request):
        user = request.user.has_perm('recrutador.add_vaga')
        if user == False:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return  render(
            request, 'recrutador/form.html')

    def post(self, request):
        user_logado = request.user.id
        recrutador = Vaga.objects.create(
            nome_da_vaga = request.POST['nome_da_vaga'],
            faixa_salarial = request.POST['faixa_salarial'],
            escolaridade_minima = request.POST['escolaridade_minima'],
            owner_id = user_logado 
            ) 
      
        return redirect('vagas_cadastradas')

class VagaUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        user = request.user.has_perm('recrutador.change_vaga')
        if user == False:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
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
        vaga.owner_id = user_logado 
        vaga.save()
        return redirect('vagas_cadastradas')

@login_required()
def vaga_delete (request, id):
    user = request.user.has_perm('recrutador.delete_vaga')
    if user == False:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    vaga = Vaga.objects.get(id = id) or None
    if request.method == 'POST':
        vaga.delete()
        return redirect('vagas_cadastradas')
    else:
        return  render(
            request, 'recrutador/confirm_delete.html')