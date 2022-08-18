from django.shortcuts import render, redirect
from django.views import View
from recrutador.models import Vaga
from candidato.models import MinhaIscricao, PretencaoSalarial, DadosPessoais

def home(request):
    if not  request.user:
        return redirect('vagas')
    else:
        return render(request,'home/home.html')
    

class Vagas(View):
    def get(self, request):
        data = {}
        data['dados_pessoais'] = DadosPessoais.objects.filter(owner_id = request.user.id)
        data['pretencao_salarial'] = PretencaoSalarial.objects.filter(owner_id = request.user.id) 
        data['vagas'] = Vaga.objects.all()
        return render(
            request, 'home/vagas.html', data)