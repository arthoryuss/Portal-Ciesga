from django.conf.urls import include, url
from django.urls import path
from . import views

app_name='vagas'

urlpatterns = [
    path("mural-de-vagas/", views.mural_de_vagas, name='mural_de_vagas'),
    path("mural-de-vagas/ver-vaga/<id>", views.requisitos, name='requisitos'),
    path("mural-de-vagas/ver-vaga/inscricao/<id>", views.inscricao, name='inscricao'),
    ]