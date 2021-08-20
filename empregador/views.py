from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.forms.models import inlineformset_factory

from usuario.models import User
from candidato.models import *
from vagas.models import Vaga, Candidatura
from .models import *
from .forms import *

User = get_user_model()

@login_required
def info_basica2(request):
    template_name = 'info_basica2.html'
    context = {}
    if request.method == 'POST':
        form1 = InfoBasicaForm(request.POST, instance=request.user.empregador)
        form2 = UserForm2(request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(
                request, 'Os dados da sua conta foram alterados com sucesso'
            )
            return redirect('usuario:dashboard')
    else:
        form1 = InfoBasicaForm(instance=request.user.empregador)
        form2 = UserForm2(instance=request.user)
    context = {

        'form1':form1,
        'form2':form2

    }
    return render(request, template_name, context)
InfoBasicaForm

#FALTA IMPLEMENTAR O FORM DINÂMICO
@login_required
def cadastrar_vaga(request):
    template_name = 'cadastrar_vaga.html'
    context = {}
    CadastrarRequisitosFormSet = inlineformset_factory(
            Vaga, 
            Requisitos,
            form=RequisitosForm,
            fields = '__all__',
            extra=3,
            can_delete = False,
            min_num = 1,
            validate_min = True,
            )
    if request.method == 'POST':
        forms = CadastrarVagaForm(request.POST, request.FILES)
        formset = CadastrarRequisitosFormSet(request.POST, request.FILES)
        if  forms.is_valid():
            vaga = forms.save(commit=False) 
            vaga.empregador = request.user.empregador
            if vaga.empregador.nome == None:
                messages.success(
                request, 'A vaga não foi criada. Para criar uma vaga é necessário antes preencher as informações básicas.'
            )
            else:
                requisito =  CadastrarRequisitosFormSet(request.POST, request.FILES, instance = vaga)
                vaga.save()
                requisito.save()
                messages.success(
                    request, 'A vaga foi criada com sucesso'
                )
                return redirect('empregador:cadastrar_vaga')
    else:
        forms = CadastrarVagaForm()
        formset = CadastrarRequisitosFormSet()
    context = {

        'forms':forms,
        'formset':formset,
    }
    return render(request, template_name, context)

def editar_vaga(request, id):
    template_name = 'editar_vaga.html'
    context = {}
    CadastrarRequisitosFormSet = inlineformset_factory(
            Vaga, 
            Requisitos,
            form=RequisitosForm,
            fields = '__all__',
            extra=3,
            can_delete = False,
            min_num = 1,
            validate_min = True,
            )
    vaga = Vaga.objects.get(id = id)
    if request.method == 'POST':
        forms = CadastrarVagaForm(request.POST, request.FILES, instance = vaga)
        formset = CadastrarRequisitosFormSet(request.POST, request.FILES, instance = vaga)
        if  forms.is_valid():
            vaga = forms.save(commit=False)
            requisito =  CadastrarRequisitosFormSet(request.POST, request.FILES, instance = vaga)
            vaga.save()
            requisito.save()
            messages.success(
                request, 'A vaga foi editada com sucesso'
            )
            return redirect('empregador:minhas_vagas')
    else:
        forms = CadastrarVagaForm(instance = vaga)
        formset = CadastrarRequisitosFormSet(instance = vaga)
    context = {

        'forms':forms,
        'formset':formset,
    }
    return render(request, template_name, context)

@login_required
def minhas_vagas(request):
    template_name = 'minhas_vagas.html'
    return render(request, template_name)


def excluir_vaga(request, id):
    vaga = Vaga.objects.get(id=id)
    if request.method == 'POST':
        form = InscritosForm(request.POST, instance = vaga)
        vaga = form.save(commit=False)
        vaga.finalizada = True
        vaga.save()
        messages.success(request, 'A vaga foi excluida com sucesso')
        return redirect('empregador:minhas_vagas')
    template = 'finalizar_vaga.html'
    form = InscritosForm()
    context = {
        'vaga': vaga,
        'form':form,
    }
    return render(request, template, context)

def status_vaga(request, id):
    dado = Vaga.objects.get(id=id)
    if dado.status:
        dado.status = False
        dado.save()
        messages.success(
            request, 'Sua vaga foi retirada do nosso mural'
        )
    else:
        dado.status = True
        dado.save()
        messages.success(
            request, 'Sua vaga agora está à mostra no nosso mural'
        )
    return redirect('empregador:minhas_vagas')

@login_required
def ver_inscritos(request, id):
    template_name = 'ver_inscritos.html'
    dado = Vaga.objects.get(id=id)
    candidaturas = Candidatura.objects.filter(vaga = dado)
    var_get_escolaridade = request.GET.get('escolaridade', None)
    var_get_genero = request.GET.get('genero', None)
    var_get_deficiente = request.GET.get('deficiente', None)
    if var_get_escolaridade or var_get_genero or var_get_deficiente:
        candidaturas = Candidatura.objects.filter(vaga = dado, 
            candidato__escolaridade__contains=var_get_escolaridade,
            candidato__genero__contains=var_get_genero,
            candidato__deficiente__contains=var_get_deficiente,
            )
    context = {
        'candidaturas':candidaturas,
    }
    return render(request, template_name, context)

@login_required
def detalhes_candidato(request, id):
    template_name = 'detalhes_candidato.html'
    candidato = Candidato.objects.get(id=id)
    formacoes = Formacao.objects.filter(candidato_id = candidato.id)
    experiencias = Experiencia.objects.filter(candidato_id = candidato.id)
    idiomas = Idioma.objects.filter(candidato_id = candidato.id)
    cursos = Curso.objects.filter(candidato_id = candidato.id)
    context = {
        'candidato':candidato,
        'formacoes':formacoes,
        'experiencias': experiencias,
        'idiomas': idiomas,
        'cursos' : cursos,
    }
    return render(request, template_name, context)

