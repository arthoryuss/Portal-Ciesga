from django.template import Library
from django.contrib.auth import authenticate, login, get_user_model

register = Library()
User = get_user_model()

from vagas.models import *
from candidato.models import Candidato
from usuario.models import User

@register.inclusion_tag('templatetags/minhas_candidaturas_tag.html')

def minhascandidaturastag(user):
	candidato = Candidato.objects.get(user_id = user.id)
	candidaturas = Candidatura.objects.filter(candidato_id = candidato.id)
	tag = []
	for candidatura in candidaturas:
		if candidatura.vaga.finalizada == False:
			tag.append(candidatura)

	context = {
        'tag': tag,
    }
	return context
