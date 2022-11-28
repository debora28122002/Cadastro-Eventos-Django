from datetime import datetime, timedelta
from django.shortcuts import render, HttpResponse, redirect
from app.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import Http404, JsonResponse

def hello(request, nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user 
    data_atual = datetime.now()
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__gt=data_atual)
    response = {'eventos': evento}
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

@login_required(login_url = '/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento']=Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url = '/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao=descricao
                evento.data_evento=data_evento
                evento.local = local
                evento.save()
        else:
            Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario,
                              local = local)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')

@login_required(login_url='/login/')
def eventos_passados(request):
    usuario = request.user 
    data_atual = datetime.now()
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__lt=data_atual)
    response = {'eventos': evento}
    return render(request, 'eventos_passados.html', response)
