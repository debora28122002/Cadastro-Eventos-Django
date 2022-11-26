from django.shortcuts import render, HttpResponse
from app.models import Evento

def hello(request, nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))

def lista_eventos(request):
    eventos = Evento.objects.all()
    response = {'eventos': eventos}
    return render(request, 'agenda.html', response)

