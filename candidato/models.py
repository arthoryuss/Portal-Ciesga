from django.db import models
import re
import datetime
from django.core import validators
from django.conf import settings
from core.choices import *
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
    UserManager)
from usuario.models import User
from municipios.models import *	

# Create your models here.

class Candidato(models.Model):

	user = models.OneToOneField(User, related_name='candidato', on_delete=models.CASCADE)
	cpf = models.CharField('CPF',max_length = 14, blank=False, unique=True)
	data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
	logradouro = models.CharField('Rua',max_length = 100, null=True, blank=True)
	numeroLog = models.CharField('Número', max_length = 10, null=True, blank=True)
	bairro = models.CharField('Bairro', max_length = 50, null=True, blank=True)
	cidade = models.CharField('Cidade', max_length = 50, null=True, blank=True)
	uf = models.CharField('UF', max_length = 50, null=True, blank=True)
	cep = models.CharField('CEP', max_length = 10, null=True, blank=True)
	complemento = models.CharField('Complemento', max_length = 100, null=True, blank=True)
	tel1 = models.CharField('Tel(1)', max_length = 12, null=True, blank=True)
	tel2 = models.CharField('Tel(2)', max_length = 12, null=True, blank=True)
	obs = models.CharField(max_length = 200, null=True, blank=True)
	
	deficiente = models.CharField(
			'Portador de deficiência',
			max_length=5,
			null=True,
			blank=True,
			choices=YESORNOT_CHOICES,
		)
	escolaridade = models.CharField(
			'Escolaridade',
			max_length=25,
			null=True,
			blank=True,
			choices=EDUCATION_CHOICES,
		)
	habilitacao = models.CharField(
			'Habilitação',
			max_length=25,
			null=True,
			blank=True,
			choices=HABILITACAO,
		)
	estado_civil = models.CharField(
			'Estado civil',
			max_length=25,
			null=True,
			blank=True,
			choices=MARITAL_STATUS,
		)	
	genero = models.CharField(
			'Gênero',
			max_length=25,
			null=True,
			blank=True,
			choices=GENDER_CHOICES,
		)			

	def __str__(self):
		return self.user.name

class Experiencia(models.Model):
	candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
	empresa = models.CharField('Empresa', max_length = 100, null=True, blank=True)
	cargo = models.CharField('Cargo', max_length = 100, null=True, blank=True)
	descricao = models.TextField ('Descrição das atividades', max_length = 1000, null=True, blank=True)
	data_entrada = models.DateField('Data da contratação', null=True, blank=True)
	data_saida = models.DateField('Data da saída', null=True, blank=True)
	def __str__(self):
		return self.cargo


class Formacao(models.Model):
	candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='formacao')
	grau = models.CharField(
			'Nível',
			max_length=25,
			null=True, 
			blank=True,
			choices=EDUCATION_CHOICES_FORMATION,
		)
	instituicao = models.CharField('Instituição' ,max_length = 100, null=True, blank=True)
	curso = models.CharField('Curso', max_length = 50, null=True, blank=True)
	data_entrada = models.DateField('Data de Entrada', null=True, blank=True)
	data_conclusao = models.DateField('Data de Saída', null=True, blank=True)
	
	def __str__(self):
		return self.curso

class Idioma(models.Model):
	candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
	idioma = models.CharField(max_length = 20, null=True, blank=True)
	nivel = models.CharField(
			max_length=25,
			null=True, 
			blank=True,
			choices=LEVEL,
		)
	def __str__(self):
		return self.idioma

class Curso(models.Model):
	candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
	tipo = models.CharField(
			'Tipo',
			max_length=25,
			null=True, 
			blank=True,
			choices=COURSE_TYPE,
		)
	curso = models.CharField('Curso',max_length=50, null=True, blank=True)
	instituicao = models.CharField('Instituição',max_length =30, null=True, blank=True)
	duracao =  models.CharField('Duração',max_length=5, null=True, blank=True)
	data_entrada = models.DateField('Data de Entrada', null=True, blank=True)
	data_saida = models.DateField('Data de Conclusão', null=True, blank=True)

	def __str__(self):
		return self.curso

class Profissoes(models.Model):
	nome_prof = models.CharField('Profissão', max_length=100, null=True, blank=True)

	def __str__(self):
		return self.nome_prof
		
	class Meta:
		ordering = ['nome_prof']
		verbose_name = 'Profissão'
		verbose_name_plural = 'Profissões'


class Pretencoes(models.Model):
	candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
	profissao = models.ForeignKey(Profissoes, on_delete=models.CASCADE)
	experiencia = models.BooleanField ('Tenho experiência na função', default=False)
	comprovacao = models.BooleanField ('Posso comprovar', default=False)

	def __str__(self):
		return self.profissao.nome_prof