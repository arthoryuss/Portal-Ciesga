from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

from dal import autocomplete

from usuario.models import User
from vagas.models import Candidatura
from .models import *
from .forms import *

User = get_user_model()

# Create your views here.
@login_required

def info_basica(request):
    template_name = 'info_basica.html'
    context = {}
    if request.method == 'POST':
        form1 = InfoBasicaForm(request.POST, instance=request.user.candidato)
        form2 = UserForm2(request.POST, instance=request.user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(
                request, 'Os dados da sua conta foram alterados com sucesso'
            )
            return redirect('usuario:dashboard')
    else:
        form1 = InfoBasicaForm(instance=request.user.candidato)
        form2 = UserForm2(instance=request.user)
    context = {

        'form1':form1,
        'form2':form2

    }
    return render(request, template_name, context)


@login_required

def formacao(request):
    template_name = 'formacao.html'
    context = {}
    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            formacao = form.save(commit=False)  
            candidato = Candidato.objects.get(user_id = request.user.id)
            formacao.candidato_id = candidato.id
            formacao.save()
            messages.success(
                request, 'As informações foram adicionadas com sucesso'
            )
            return redirect('candidato:formacao')
    else:
        form = FormacaoForm()
    context = {

        'form':form,
    }
    return render(request, template_name, context)


@login_required

def experiencia(request):
    template_name = 'experiencia.html'
    context = {}
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            experiencia = form.save(commit=False)  
            candidato = Candidato.objects.get(user_id = request.user.id)
            experiencia.candidato_id = candidato.id
            experiencia.save()
            messages.success(
                request, 'As informações foram adicionadas com sucesso'
            )
            return redirect('candidato:experiencia')
    else:
        form = ExperienciaForm()
    context = {

        'form':form,

    }
    return render(request, template_name, context)

@login_required

def curso(request):
    template_name = 'curso.html'
    context = {}
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)  
            candidato = Candidato.objects.get(user_id = request.user.id)
            curso.candidato_id = candidato.id
            curso.save()
            messages.success(
                request, 'As informações foram adicionadas com sucesso'
            )
            return redirect('candidato:curso')
    else:
        form = CursoForm()
    context = {

        'form':form,

    }
    return render(request, template_name, context)


@login_required

def idioma(request):
    template_name = 'idioma.html'
    context = {}
    if request.method == 'POST':
        form = IdiomaForm(request.POST)
        if form.is_valid():
            idioma = form.save(commit=False)  
            candidato = Candidato.objects.get(user_id = request.user.id)
            idioma.candidato_id = candidato.id
            idioma.save()
            messages.success(
                request, 'As informações foram adicionadas com sucesso'
            )
            return redirect('candidato:idioma')
    else:
        form = IdiomaForm()
    context = {

        'form':form,

    }
    return render(request, template_name, context)
IdiomaForm

@login_required

def excluir_experiencia(request, id):
    dado = Experiencia.objects.get(id=id)
    dado.delete()
    messages.success(
            request, 'A experiência foi excluída com sucesso'
        )
    return redirect('candidato:experiencia')

@login_required

def excluir_formacao(request, id):
    dado = Formacao.objects.get(id=id)
    dado.delete()
    messages.success(
            request, 'A formação foi excluída com sucesso'
        )
    return redirect('candidato:formacao')

@login_required

def excluir_curso(request, id):
    dado = Curso.objects.get(id=id)
    dado.delete()
    messages.success(
            request, 'A formação foi excluída com sucesso'
        )
    return redirect('candidato:curso')

@login_required

def excluir_idioma(request, id):
    dado = Idioma.objects.get(id=id)
    dado.delete()
    messages.success(
            request, 'O idioma foi excluído com sucesso'
        )
    return redirect('candidato:idioma')

@login_required

def editar_experiencia(request, id):
    template_name = 'experiencia_editar.html'
    context = {}
    if request.method == 'POST':
        form = ExperienciaForm(request.POST, instance = Experiencia.objects.get(id=id))
        if form.is_valid():
            form.save()  
            messages.success(
                request, 'Os dados foram atualizados com sucesso'
            )
            return redirect('candidato:experiencia')
    else:
        dado = Experiencia.objects.get(id=id)
        form = ExperienciaForm(instance = dado)
        context = {

            'form':form,

        }
    return render(request, template_name, context)


@login_required

def editar_idioma(request, id):
    template_name = 'idioma_editar.html'
    context = {}
    if request.method == 'POST':
        form = IdiomaForm(request.POST, instance = Idioma.objects.get(id=id))
        if form.is_valid():
            form.save()  
            messages.success(
                request, 'Os dados foram atualizados com sucesso'
            )
            return redirect('candidato:idioma')
    else:
        dado = Idioma.objects.get(id=id)
        form = IdiomaForm(instance = dado)
        context = {

            'form':form,

        }
    return render(request, template_name, context)

@login_required

def editar_formacao(request, id):
    template_name = 'formacao_editar.html'
    context = {}
    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance = Formacao.objects.get(id=id))
        if form.is_valid():
            form.save()  
            messages.success(
                request, 'Os dados foram atualizados com sucesso'
            )
            return redirect('candidato:formacao')
    else:
        dado = Formacao.objects.get(id=id)
        form = FormacaoForm(instance = dado)
        context = {

            'form':form,

        }
    return render(request, template_name, context)

@login_required

def editar_curso(request, id):
    template_name = 'curso_editar.html'
    context = {}
    if request.method == 'POST':
        form = CursoForm(request.POST, instance = Curso.objects.get(id=id))
        if form.is_valid():
            form.save()  
            messages.success(
                request, 'Os dados foram atualizados com sucesso'
            )
            return redirect('candidato:curso')
    else:
        dado = Curso.objects.get(id=id)
        form = CursoForm(instance = dado)
        context = {

            'form':form,

        }
    return render(request, template_name, context)

@login_required

def minhas_candidaturas(request):
    template_name = 'minhas_candidaturas.html'
    return render(request, template_name)

@login_required

def excluir_candidatura(request, id):
    dado = Candidatura.objects.get(id=id)
    dado.delete()
    messages.success(
            request, 'Sua inscrição foi cancelada com sucesso'
        )
    return redirect('candidato:minhas_candidaturas')

@login_required
def pretencoes(request):
    template_name = 'pretencoes.html'
    context = {}
    if request.method == 'POST':
        form = PretencoesForm(request.POST)
        if form.is_valid():
            pretencao = form.save(commit=False)  
            candidato = Candidato.objects.get(user_id = request.user.id)
            pretencao.candidato_id = candidato.id
            pretencao.save()
            messages.success(
                request, 'As informações foram adicionadas com sucesso'
            )
            return redirect('candidato:pretencoes')
    else:
        form = PretencoesForm()
    context = {

        'form':form,

    }
    return render(request, template_name, context)

@login_required
def editar_pretencao(request, id):
    template_name = 'editar_pretencao.html'
    context = {}
    if request.method == 'POST':
        form = PretencoesForm(request.POST, instance = Pretencoes.objects.get(id=id))
        if form.is_valid():
            form.save()  
            messages.success(
                request, 'Os dados foram atualizados com sucesso'
            )
            return redirect('candidato:pretencoes')
    else:
        dado = Pretencoes.objects.get(id=id)
        form = PretencoesForm(instance = dado)
        context = {

            'form':form,

        }
    return render(request, template_name, context)

@login_required
def excluir_pretencao(request, id):
    dado = Pretencoes.objects.get(id=id)
    dado.delete()
    messages.success(
        request, 'A pretenção foi excluída com sucesso'
        )
    return redirect('candidato:pretencoes')

#class PretencoesAutocomplete(autocomplete.Select2QuerySetView):
#    def get_queryset(self):
#        # Don't forget to filter out results depending on the visitor !
#        if not self.request.user.is_authenticated():
#            return Pretencoes.objects.none()
#
#        qs = Pretencoes.objects.all()
#
#        if self.q:
#            qs = qs.filter(nome_prof__istartswith=self.q)
#
#        return qs