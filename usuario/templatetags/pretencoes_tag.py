from django.template import Library

register = Library()

from candidato.models import *
from usuario.models import User

@register.inclusion_tag('templatetags/pretencoes_tag.html')

def pretencoestag(user):
    pretencoes = Pretencoes.objects.filter(candidato = user.candidato)
    context = {
        'pretencoes': pretencoes
    }
    return context
