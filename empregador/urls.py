from django.conf.urls import include, url
from django.urls import path
from . import views

app_name='empregador'

urlpatterns = [
    path("info-basica", views.info_basica2, name='info_basica2'),
    path("cadastrar-vaga", views.cadastrar_vaga, name='cadastrar_vaga'),
    path("minhas-vagas", views.minhas_vagas, name='minhas_vagas'),
    path("minhas-vagas/excluir-vagas/<id>", views.excluir_vaga, name='excluir_vaga'),
    path("minhas-vagas/editar-vaga/<id>", views.editar_vaga, name='editar_vaga'),
    path("minhas-vagas/status-vagas/<id>", views.status_vaga, name='status_vaga'),
    path("minhas-vagas/ver-inscritos/<id>/", views.ver_inscritos, name='ver_inscritos'),
    path("minhas-vagas/ver-inscritos/detalhes/<id>", views.detalhes_candidato, name='detalhes_candidato'),
]
