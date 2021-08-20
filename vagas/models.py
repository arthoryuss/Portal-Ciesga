from django.db import models
from usuario.models import User
from candidato.models import Candidato
from empregador.models import Empregador 
from core.choices import *

# Create your models here.

class Vaga (models.Model):

	empregador = models.ForeignKey(Empregador, related_name='empregador', on_delete=models.CASCADE) 
	funcao = models.CharField ('Função', max_length = 50)
	descricao = models.TextField ('Descrição das Atividades', max_length = 1000, blank = False)
	confidencial = models.BooleanField ('Confidencial', default=False)
	data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
	ultima_modificacao = models.DateTimeField('Última Modificação', auto_now_add=False, auto_now=True)
	status = models.BooleanField ('Está ativa?', blank=True, default=True)
	finalizada = models.BooleanField ('Foi finalizada?', blank=True, default=False)
	inscritos = models.PositiveSmallIntegerField ('Quantidade de inscritos', blank=True, null=True)
	salario = models.CharField ('Salário', max_length = 20, blank=True, null=True)
	local = models.CharField ('Cidade', max_length = 50)
	escolaridade = models.CharField(
			'Escolaridade exigida',
			max_length=25,
			null=True,
			blank=True,
			choices=EDUCATION_CHOICES,
		)
	

	def __str__(self):
		return self.funcao

	def get_vaga_detail_url(self):
		return u"/vagas/%i" % self.id

class Requisitos (models.Model):

	vaga = models.ForeignKey(Vaga, related_name='vaga_requisito', on_delete=models.CASCADE)
	requisito = models.TextField('Requisito', max_length=300)

	def __str__(self):
		return self.requisito

class Candidatura (models.Model):

	candidato =  models.ForeignKey(Candidato, related_name='candiato', on_delete=models.CASCADE)
	vaga = models.ForeignKey(Vaga, related_name='vaga', on_delete=models.CASCADE)
	#data_inscricao = models.DateTimeField('Data da Inscrição', auto_now_add=True)

	def __str__(self):
		return self.candidato.user.name



