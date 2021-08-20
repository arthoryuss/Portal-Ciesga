from django.template import Library

register = Library()

from candidato.models import *
from usuario.models import User

@register.inclusion_tag('templatetags/formacoes_tag.html')

def formacoestag(user):
    formacoes = Formacao.objects.filter(candidato = user.candidato)
    context = {
        'formacoes': formacoes
    }
    return context

			