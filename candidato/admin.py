from django.contrib import admin
from usuario.forms import UserAdminCreationForm, UserForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.conf import settings

from .models import Experiencia, Formacao, Idioma, Candidato, Curso, Profissoes, Pretencoes
from usuario.models import User


class ExperienciaInline(admin.StackedInline):
	model = Experiencia

class FormacaoInline(admin.StackedInline):
	model = Formacao

class IdiomaInline(admin.StackedInline):
	model = Idioma

class CursoInline(admin.StackedInline):
	model = Curso

class PretencoesInline(admin.StackedInline):
	model = Pretencoes

class CandidatoAdmin(admin.ModelAdmin):
	inlines = (ExperienciaInline, FormacaoInline, IdiomaInline, CursoInline, PretencoesInline )

class OcupacoesAdmin(admin.ModelAdmin):
	model = Profissoes


admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Profissoes, OcupacoesAdmin)