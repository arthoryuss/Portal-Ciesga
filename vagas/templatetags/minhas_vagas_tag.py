from django.template import Library
from django.contrib.auth import authenticate, login, get_user_model

register = Library()
User = get_user_model()

from vagas.models import *
from empregador.models import Empregador
from usuario.models import User

@register.inclusion_tag('templatetags/minhas_vagas_tag.html')

def minhasvagastag(user):
	empregador = Empregador.objects.get(user_id = user.id)
	vagas = Vaga.objects.filter(empregador_id = empregador.id, finalizada = False).order_by('-data_criacao')
	context = {
        'vagas': vagas,
    }
	return context
