from django.db import models
from django.core import validators
from django.conf import settings
from usuario.models import User
from core.choices import BRANCH_ACTIVITY, BRANCH_TYPE

# Create your models here.
class Empregador(models.Model):

	user = models.OneToOneField (User, related_name='empregador', on_delete=models.CASCADE)
	cnpj = models.CharField('CNPJ', max_length = 18, blank = False)
	nome = models.CharField('Nome Fantasia',max_length = 50,null=True, blank=True)
	ramo = models.CharField(
			'Ramo de Atividade',
			max_length=25,
			null=True,
			blank=True,
			choices=BRANCH_ACTIVITY,
		)
	tipo = models.CharField(
			'Tipo da Empresa',
			max_length=25,
			null=True,
			blank=True,
			choices=BRANCH_TYPE,
		)
	tel1 = models.CharField('Tel(1)',max_length = 12,null=True, blank=True)
	tel2 = models.CharField('Tel(2)',max_length = 12, null=True, blank=True)
	logradouro = models.CharField('Endereço',max_length = 100, null=True, blank=True)
	numeroLog = models.CharField('Número', max_length = 10, null=True, blank=True)
	bairro = models.CharField('Bairro', max_length = 50, null=True, blank=True)
	complemento = models.CharField('Complemento', max_length = 100, null=True, blank=True)
	cep = models.CharField('CEP', max_length = 10, null=True, blank=True)
	cidade = models.CharField('Cidade', max_length = 50, null=True, blank=True)
	uf = models.CharField('UF', max_length = 50, null=True, blank=True)



	def __str__(self):
		return self.nome
	