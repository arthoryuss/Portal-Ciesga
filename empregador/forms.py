from .models import *
from usuario.models import User
from django.conf import settings
from django.forms import *
from django.contrib.auth import get_user_model
from django.contrib.localflavor.br.forms import BRCPFField,BRCNPJField


from vagas.models import Vaga, Requisitos, Candidatura
from core.choices import *

User = get_user_model()

class InfoBasicaForm(ModelForm):

	cnpj = BRCNPJField(label = '* CNPJ',max_length = 18 , min_length = 14)
	nome = CharField(label = '* Nome Fantasia', max_length = 50, required = True)
	ramo = ChoiceField(
		label = '* Ramo de Atividade', 
		required = True, 
		choices = BRANCH_ACTIVITY,
		)
	tipo = ChoiceField(
		label = '* Tipo da Empresa', 
		required = True, 
		choices = BRANCH_TYPE,
		)

	class Meta:
		model = Empregador
		exclude = ['user']

class UserForm2(ModelForm):

	name = CharField(label = 'Nome do Operador', max_length = 50)
	class Meta:
		model = User
		fields = ['name', 'email']

class CadastrarVagaForm(ModelForm):
	
	escolaridade = ChoiceField(
			label ='Escolaridade exigida',
			required=False,
			choices=EDUCATION_CHOICES,
			help_text = '*ATENÇÃO* Apenas candidatos com a escolaridade igual ou superior a informada neste campo poderão se candidatar a vaga. Caso queira abrir a inscrição a todos, deixe esse campo em branco.'
		)
	salario = CharField(
			label = 'Salário',
			max_length = 20, 
			required = False,
			help_text = "Ex: 1.500,00. Caso deseje o status 'a combinar', deixe este campo em branco."
		)
	confidencial = BooleanField(
			label = 'Confidencial',
			required = False,
			help_text = 'Marque esta opção caso não deseje divulgar o nome de sua empresa.',
			widget= CheckboxInput()
		)

	class Meta:
		model = Vaga
		exclude = ['empregador', 'status','inscritos','finalizada']

class RequisitosForm(ModelForm):
	requisito = CharField(
		label = 'Requisito',
		max_length = 300,
		required = False,
		widget= Textarea(attrs = {'rows':4, 'cols':15})
				)
	class Meta:
		model = Requisitos
		exclude = ['vaga']


class InscritosForm(ModelForm):
	inscritos = IntegerField(
		label = 'Quantidade de candidatos selecionados',
		required = False,
	)
	class Meta:
		model = Vaga
		fields = ['inscritos']
