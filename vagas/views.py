from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *

User = get_user_model()

# Create your views here.

@login_required

def mural_de_vagas(request):
	vagas_list = Vaga.objects.filter(status = True, finalizada = False).order_by('-data_criacao')
	var_get_search = request.GET.get('search_box', None)
	if var_get_search:
		vagas_list = Vaga.objects.filter(status = True, finalizada = False, funcao__icontains=var_get_search).order_by('-data_criacao')
	paginator = Paginator(vagas_list, 15)


	try:
		page = (request.GET.get('page', '1'))
	except ValueError:
		page = 1
	try:
		vagas = paginator.page(page)
	except (EmptyPage, InvalidPage):
		vagas = paginator.page(1)

	index = vagas.number - 1
	max_index = len(paginator.page_range)
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	page_range = paginator.page_range[start_index:end_index]

	template_name = 'mural_de_vagas.html'
	return render(request, template_name,{ 
        'vagas': vagas,
        'page_range': page_range,
        })

@login_required

def requisitos(request, id):
	template_name = 'vaga.html'
	vaga = Vaga.objects.get(id=id)
	requisitos = Requisitos.objects.filter(vaga_id = id)
	context = {
            'vaga':vaga,
            'requisitos':requisitos,
        }
	return render(request, template_name, context)
	
@login_required

def inscricao(request, id):
	template_name = 'mural_de_vagas.html'
	vaga = Vaga.objects.get(id=id)
	user=request.user 

	if user.user_type == "Candidato":
		candidato = user.candidato
		tag = 0 
		tag2 = 0

		if candidato.escolaridade  == 'Fundamental incompleto':
			tag = 1
		elif candidato.escolaridade == 'Fundamental completo':
			tag = 2
		elif candidato.escolaridade == 'Medio incompleto':
			tag = 3
		elif candidato.escolaridade == 'Medio completo':
			tag = 4
		elif candidato.escolaridade == 'Tecnico incompleto':
			tag = 5
		elif candidato.escolaridade == 'Tecnico completo':
			tag = 6
		elif candidato.escolaridade == 'Superior incompleto':
			tag = 7
		elif candidato.escolaridade == 'Superior completo':
			tag = 8
		elif candidato.escolaridade == 'Pos-Graduacao':
			tag = 9
		elif candidato.escolaridade == 'Mestrado':
			tag = 10
		elif candidato.escolaridade == 'Doutorado':
			tag = 11
		else:
			tag = 12

		if vaga.escolaridade == 'Fundamental incompleto' or vaga.escolaridade == '':
			tag2 = 1
		elif vaga.escolaridade == 'Fundamental completo':
			tag2 = 2
		elif vaga.escolaridade == 'Medio incompleto':
			tag2 = 3
		elif vaga.escolaridade == 'Medio completo':
			tag2 = 4
		elif vaga.escolaridade == 'Tecnico incompleto':
			tag2 = 5
		elif vaga.escolaridade == 'Tecnico completo':
			tag2 = 6
		elif vaga.escolaridade == 'Superior incompleto':
			tag2 = 7
		elif vaga.escolaridade == 'Superior completo':
			tag2 = 8
		elif vaga.escolaridade == 'Pos-Graduacao':
			tag2 = 9
		elif vaga.escolaridade == 'Mestrado':
			tag2 = 10
		elif vaga.escolaridade == 'Doutorado':
			tag2 = 11
		else:
			tag2 = 12

		if candidato.escolaridade == None:
			messages.info(
		                request, 'Inscrição não realizada. Preencha suas informações básicas para poder candidatar-se as vagas.'
		            )

		elif tag >= tag2:
		 	inscricao, criado = Candidatura.objects.get_or_create(candidato = candidato, vaga = vaga)
		 	if  criado:
		 		messages.success(
		                request, 'A sua inscrição foi realizada com sucesso.'
		            )
		 	else:
		 		messages.success(
		                request, 'Você já se cadastrou nessa vaga. Acompanhe suas candidaturas pelo Painel.'
		            )
		else:
			messages.success(
		                request, 'Você não possui a escolaridade mínima exigida para essa vaga.'
		            )

		return redirect('vagas:mural_de_vagas')
	else:
		messages.info(
	                request, 'Apenas usuários do tipo candidato podem se candidatar em vagas de emprego.'
	            )
		return redirect('vagas:mural_de_vagas')
