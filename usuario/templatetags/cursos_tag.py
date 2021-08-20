from django.template import Library

register = Library()

from candidato.models import *
from usuario.models import User

@register.inclusion_tag('templatetags/cursos_tag.html')

def cursostag(user):
    cursos = Curso.objects.filter(candidato = user.candidato)
    context = {
        'cursos': cursos
    }
    return context
