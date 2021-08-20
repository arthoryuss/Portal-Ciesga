from django.template import Library

register = Library()

from candidato.models import *
from usuario.models import User

@register.inclusion_tag('templatetags/experiencia_tag.html')


def experienciastag(user):
    experiencias = Experiencia.objects.filter(candidato = user.candidato)
    context = {
        'experiencias': experiencias,
    }
    return context

