from django.template import Library
from django.contrib.auth import authenticate, login, get_user_model

register = Library()
User = get_user_model()

from vagas.models import *
from empregador.models import Empregador
from usuario.models import User

@register.inclusion_tag('templatetags/vaga_tag.html')


def vagastag(user):

	vagas = Vaga.objects.filter(status = True, finalizada = False).order_by('-data_criacao')
	context = {
		  'vagas': vagas,
	}
	
	return context
	



