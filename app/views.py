from django.shortcuts import render, HttpResponse, redirect
from app.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def hello(request, nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))

@login_required(login_url='/login/')
def lista_eventos(request):
    eventos = Evento.objects.all()
    response = {'eventos': eventos}
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    return render(request, 'agenda.html', response)

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        
        else:
            messages.error(request, "Usuário ou senha inválida!")
            return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')
