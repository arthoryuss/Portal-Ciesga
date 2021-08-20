from django.conf.urls import include, url
from django.urls import path
from . import views
#from .views import PretencoesAutocomplete
from .models import Profissoes, Pretencoes
from dal import autocomplete

app_name='candidato'    

urlpatterns = [
    path("info_basica", views.info_basica, name='info_basica'),
    path("formacao", views.formacao, name='formacao'),
    path("formacao/excluir-formacao/<id>", views.excluir_formacao, name='excluir_formacao'),
    path("formacao/editar-formacao/<id>", views.editar_formacao, name='editar_formacao'),
    path("experiencia", views.experiencia, name='experiencia'),
    path("experiencia/excluir-experiencia/<id>", views.excluir_experiencia, name='excluir_experiencia'),
    path("experiencia/editar-experiencia/<id>", views.editar_experiencia, name='editar_experiencia'),
    path("curso", views.curso, name='curso'),
    path("curso/excluir-curso/<id>", views.excluir_curso, name='excluir_curso'),
    path("curso/editar-curso/<id>", views.editar_curso, name='editar_curso'),
    path("idioma", views.idioma, name='idioma'),
    path("idioma/excluir-idioma/<id>", views.excluir_idioma, name='excluir_idioma'),
    path("idioma/editar-idioma/<id>", views.editar_idioma, name='editar_idioma'),
    path("pretencoes", views.pretencoes, name='pretencoes'),
    path("idioma/excluir-pretencao/<id>", views.excluir_pretencao, name='excluir_pretencao'),
    path("idioma/editar-pretencao/<id>", views.editar_pretencao, name='editar_pretencao'),
    #path("ocupacao-autocomplete", views.PretencoesAutocomplete, name='ocupacao_autocomplete'),
    path('ocupacao-autocomplete',autocomplete.Select2QuerySetView.as_view(model=Profissoes), name='select2_fk'),
    path("minhas-candidaturas", views.minhas_candidaturas, name='minhas_candidaturas'),
    path("minhas-candidaturas/excluir-candidatura/<id>", views.excluir_candidatura, name='excluir_candidatura'),
]




