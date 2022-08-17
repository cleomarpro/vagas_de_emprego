from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from candidato.models import Experiencia, Escolaridade, DadosPessoais
from django.contrib.auth.models import Permission
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
                nome = request.POST['first_name'],
                segundo_nome = request.POST['last_name'],
                email = request.POST['email'],
                owner_id = usuario.id
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
            # Atribuindo permissões ao usuário cadastrado
            permissao1 = Permission.objects.get(codename='add_vaga')
            permissao2 = Permission.objects.get(codename='change_vaga')
            permissao3 = Permission.objects.get(codename='delete_vaga')
            permissao4 = Permission.objects.get(codename='view_vaga')
            usuario.user_permissions.add(
                permissao1, 
                permissao2,
                permissao3,
                permissao4
                )
            return redirect('vagas_cadastradas')
       