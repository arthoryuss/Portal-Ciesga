from django.contrib import admin
from candidato.models import Candidato
from empregador.models import Empregador
from .models import *

# Register your models here.

class RequisitosInline(admin.StackedInline):
	model = Requisitos

class VagaAdmin(admin.ModelAdmin):
	inlines = (RequisitosInline,)

class CandidaturaAdmin(admin.ModelAdmin):
	model = Candidatura

admin.site.register(Vaga, VagaAdmin)
admin.site.register(Candidatura, CandidaturaAdmin)