from django.db import models
import re
import datetime
from django.core import validators
from django.conf import settings
from core.choices import *
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
    UserManager)
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'Usuário', max_length=30, unique=True, validators=[username_validator],
    )
    name = models.CharField('Nome Completo', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    user_type = models.CharField( 
    		'Tipo de Usuário',
			max_length=25,
			blank=False,
			choices=USER_TYPE,
		)			
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class PasswordReset(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuario',
        #related_name='resets',
        on_delete=models.CASCADE,
    )
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at']
