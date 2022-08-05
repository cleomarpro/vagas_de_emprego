from django.shortcuts import render
from django.views import View

class UsuarioCreate(View):
    def get(self, request):
        
        return render(
            request, 'usuarios/cadastro.html')