from django.shortcuts import render
from django.views import View
from recrutador.models import Vaga

def home(request):
    return render(request,'home/home.html')

class Vagas(View):
    def get(self, request):
        data = {}
        data['vagas'] = Vaga.objects.all()
        return render(
            request, 'home/vagas.html', data)