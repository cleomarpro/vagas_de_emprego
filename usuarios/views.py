from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from candidato.models import Experiencia, Escolaridade, DadosPessoais
import datetime

class CandidatoUserCreate( View):
    def get(self, request):

        return render(
            request, 'usuarios/candidato.html')
    
    def post(self, request):
        data = {}
        email = User.objects.filter(username= request.POST['email'])or 0
        if email != 0:
            data['mensagen_de_erro_email'] = 'E-mail já existe!'
            return render(
                request, 'usuarios/candidato.html', data)
        else:
            usuario = User.objects.create_user(
                password= request.POST['password'],
                username= request.POST['email'],
            )
            dados_pessoais = DadosPessoais.objects.create(
                nome = request.POST['nome'],
                segundo_nome = request.POST['segundo_nome'],
                email = request.POST['email'],
                owner = usuario.id
                )
            return redirect('login') 
            

class RecrutadorUseCreate(View):
    def get(self, request):

        
        return render(
            request, 'usuarios/recrutador.html')
    
    def post(self, request):
        data = {}
        email = User.objects.filter(email= request.POST['email'])or 0
        if email != 0:
            data['mensagen_de_erro_email'] = 'E-mail já existe!'
            return render(
                request, 'usuarios/recrutador.html', data)

        else:
            
            usuario = User.objects.create_user(
                    email = request.POST['email'],
                    password = request.POST['password'],
                    username = request.POST['email'],
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    )
            return redirect('vagas_cadastradas')
       