from django.template import Library

register = Library()

from candidato.models import *
from usuario.models import User

@register.inclusion_tag('templatetags/idioma_tag.html')

def idiomastag(user):
    idiomas = Idioma.objects.filter(candidato = user.candidato)
    context = {
        'idiomas': idiomas
    }
    return context