from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def cadastrar(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')

    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = User.objects.filter(username=username).first()

    if user:
        return HttpResponse('Já existe um usuário com esse username')

    user = User.objects.create_user(
        username=username,
        email=email,
        password=senha
    )

    return HttpResponse("Usuário cadastrado com sucesso")


def login_view(request):

    if request.method == "GET":
        return render(request, 'login.html')

    username = request.POST.get('username')
    senha = request.POST.get('senha')

    user = authenticate(username=username, password=senha)

    if user:
        login(request, user)
        return HttpResponse("Autenticado")

    return HttpResponse("Nome de usuário ou senha inválidos")

@login_required(login_url="/autor/login/")
def text_plataforma(request):
    return HttpResponse('Isto significa que você está logado!')