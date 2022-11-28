from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import RedirectView
from django.http.response import Http404

try:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('hello/<nome>/', views.hello),
        path('agenda/', views.lista_eventos),
        path('', RedirectView.as_view(url='/agenda/')),
        path('login/', views.login_user),
        path('login/submit', views.submit_login),
        path('logout/', views.logout_user),
        path('agenda/evento/', views.evento),
        path('agenda/evento/submit', views.submit_evento),
        path('agenda/evento/delete/<int:id_evento>', views.delete_evento),
        path('agenda/eventos_passados/', views.eventos_passados),
    ]
except Exception:
        raise Http404()
