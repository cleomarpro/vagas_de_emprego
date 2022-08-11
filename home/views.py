from django.shortcuts import render, redirect
from django.views import View
from recrutador.models import Vaga
from candidato.models import MinhaIscricao

def home(request):
    if not  request.user:
        return redirect('vagas')
    else:
        return render(request,'home/home.html')
    

class Vagas(View):
    def get(self, request):
        data = {}
        data['vagas'] = Vaga.objects.all()
        return render(
            request, 'home/vagas.html', data)