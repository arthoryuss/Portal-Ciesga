from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

from core.utils import generate_hash_key

from .forms import RegisterForm, PasswordResetForm, Register_EmpregadorForm
from .models import PasswordReset, User

User = get_user_model()

# Create your views here.
def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('usuario:dashboard')
    else:
        form = RegisterForm()

    context = {
        'form': form,

    }
    return render(request, template_name, context)

def register_empregador(request):
    template_name = 'register_empregador.html'
    context = {}
    if request.method == 'POST':
        form = Register_EmpregadorForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('usuario:dashboard')
    else:
        form = Register_EmpregadorForm()

    context = {
        'form': form,

    }
    return render(request, template_name, context)

    
def password_reset(request):
    template_name = 'password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


@login_required
def dashboard(request):
    
    user=request.user 
    if user.user_type == 'Candidato':
        template_name = 'dashboard_candidato.html'
        context = {}
        return render(request, template_name, context)
    else :
        template_name = 'dashboard_empregador.html'
        context = {}
        return render(request, template_name, context)


@login_required
def edit_password(request):

    user = request.user
    if user.user_type == 'Candidato':
        template_name = 'edit_password.html'
    else:
        template_name = 'edit_password_empregador.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

def choice_register(request):
   return render(request, 'choice_register.html')
