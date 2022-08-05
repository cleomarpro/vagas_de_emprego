from django.shortcuts import render
from django.views import View

class MinhasVagas(View):
    def get(self, request):
        
        return render(
            request, 'candidato/minhas_vagas.html')