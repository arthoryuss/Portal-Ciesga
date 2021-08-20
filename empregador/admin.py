from django.contrib import admin
from .models import Empregador
from vagas.models import *


class VagaInline(admin.StackedInline):
	model = Vaga

class EmpregadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'bairro')
    inlines = (VagaInline,)

admin.site.register(Empregador, EmpregadorAdmin)