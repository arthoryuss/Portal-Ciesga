from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from usuario.forms import User
from .models import Candidato, Experiencia, Formacao, Idioma, Curso, Profissoes, Pretencoes
from django.forms import *
from django.contrib.localflavor.br.forms import BRCPFField,BRCNPJField
#from municipios.widgets import SelectMunicipioWidget
from core.choices import *
#from dal import autocomplete

User = get_user_model()

class InfoBasicaForm(ModelForm):

	cpf = BRCPFField(label = 'CPF*',max_length = 14 , min_length = 11)
	bairro = CharField(label ='Bairro*', required = True)
	cidade = CharField(label ='Cidade*', required = True)
	uf = CharField(label ='UF*', required = True )
	tel1 = CharField(label ='Tel(1)*', required = True)
	#cidade = IntegerField(widget=SelectMunicipioWidget)
	deficiente = ChoiceField(
		label = 'Portador de deficiência*', 
		required = True, 
		choices = YESORNOT_CHOICES,
		)
	data_nascimento = DateField( 
		widget= TextInput(attrs={"onkeypress": "return dateMask(this, event);","name":"datNascimento", "id":"datNascimento", "type":"text", "maxlength":"10" } ),
		label ='Data de Nascimento*', 
		help_text = 'Ex: dd/mm/aaaa',
		required = True,
		)
	escolaridade = ChoiceField(
		label = 'Escolaridade*', 
		required = True, 
		choices = EDUCATION_CHOICES
		)
	genero = ChoiceField(
		label = 'Gênero*', 
		required = True, 
		choices = GENDER_CHOICES
		)

	class Meta:
		model = Candidato
		exclude = ['obs', 'user']

        
class UserForm2(ModelForm):

	name = CharField(label ='Nome Completo/Social*', required = True)
	email = CharField(label ='E-mail*', required = True)

	class Meta:
		model = User
		fields = ['name', 'email']

class FormacaoForm(ModelForm):

	instituicao = CharField(label ='Instituição*', required = True)
	curso = CharField(label ='Curso*', required = True)
	data_entrada = DateField(
		widget= TextInput(attrs={"onkeypress": "return dateMask(this, event);","name":"datNascimento", "id":"datNascimento", "type":"text", "maxlength":"10" } ),
		label = 'Data da entrada*', 
		required = True, 
		help_text = 'Ex: dd/mm/aaaa')
	data_conclusao = DateField(
		widget= TextInput(attrs={"onkeypress": "return dateMask(this, event);","name":"datNascimento", "id":"datNascimento", "type":"text", "maxlength":"10" } ),
		label = 'Data da conclusão', 
		required = False, 
		help_text = 'Caso não tenha concluído, deixe esse campo em branco.')
	grau = ChoiceField(label ='Nível*', required = True, choices = EDUCATION_CHOICES_FORMATION)

	class Meta:
		model = Formacao
		exclude = ['candidato']

class ExperienciaForm(ModelForm):

	empresa = CharField(label ='Empresa*', required = True)
	cargo = CharField(label ='Cargo*', required = True)
	data_entrada = DateField(
		widget= TextInput(attrs={"onkeypress": "return dateMask(this, event);","name":"datNascimento", "id":"datNascimento", "type":"text", "maxlength":"10" } ),
		label = 'Data da contratação*', 
		required = True, 
		help_text = 'Ex: dd/mm/aaaa')
	data_saida = DateField(
		widget= TextInput(attrs={"onkeypress": "return dateMask(this, event);","name":"datNascimento", "id":"datNascimento", "type":"text", "maxlength":"10" } ),
		label = 'Data da saída', 
		required = False, 
		help_text = 'Caso ainda esteja nesta função, deixe esse campo em branco.')


	class Meta:
		model = Experiencia
		exclude = ['candidato']

class CursoForm(ModelForm):

	tipo = ChoiceField(label ='Tipo*', required = True, choices = COURSE_TYPE)
	curso = CharField(label ='Curso*', required = True)
	instituicao = CharField(label ='Instituição*', required = True)
	duracao = CharField(label ='Duração*', required = True, help_text = 'Em horas inteiras. Somente Números.')
	data_entrada = DateField(
		widget= TextInput(attrs={"onkeypress": "return dateMask(this, event);","name":"datNascimento", "id":"datNascimento", "type":"text", "maxlength":"10" } ),
		label = 'Data da entrada*', 
		required = True, 
		help_text = 'Ex: dd/mm/aaaa')
	data_saida = DateField(
		widget= TextInput(attrs={"onkeypress": "return dateMask(this, event);","name":"datNascimento", "id":"datNascimento", "type":"text", "maxlength":"10" } ),
		label = 'Data da conclusão', 
		required = False, 
		help_text = 'Caso não tenha concluído, deixe esse campo em branco.')
	

	class Meta:
		model = Curso
		exclude = ['candidato']

class IdiomaForm(ModelForm):

	idioma = CharField(label ='Idioma*', required = True)
	nivel = ChoiceField(label ='Nível*', required = True, choices = LEVEL)

	class Meta:
		model = Idioma
		exclude = ['candidato']


class PretencoesForm(ModelForm):

	profissao = ModelChoiceField  (
		label = 'Ocupação',
        queryset = Profissoes.objects.all(),
        #widget = autocomplete.Select2(url='candidato:select2_fk'),
    )

	class Meta:
		model = Pretencoes
		exclude = ['candidato']