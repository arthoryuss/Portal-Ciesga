from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from candidato.models import *
from empregador.models import *

from core.utils import generate_hash_key
from core.mail import send_mail_template

from .models import PasswordReset
from django.contrib.localflavor.br.forms import BRCPFField,BRCNPJField
#from captcha.fields import CaptchaField


User = get_user_model()


class RegisterForm(forms.ModelForm):

    cpf = BRCPFField(label = 'CPF',max_length = 14 , min_length = 11)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput
    )
    #captcha = CaptchaField()
    
    def clean_cpf(self):
        cpf=self.cleaned_data['cpf']
        if Candidato.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('CPF já cadastrado')
        return cpf

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2

    def save(self, commit=True):    
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.user_type = "Candidato"
        if commit:
            user.save()
            candidato = Candidato()
            candidato.user_id = user.id
            candidato.cpf = self.cleaned_data['cpf']
            candidato.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']

class Register_EmpregadorForm(forms.ModelForm):

    cnpj = BRCNPJField(label = 'CNPJ',max_length = 18 , min_length = 14)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput
    )
    #captcha = CaptchaField()
    
    def clean_cpf(self):
        cpf=self.cleaned_data['cpf']
        if Candidato.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('CPF já cadastrado')
        return cpf

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2

    def save(self, commit=True):    
        user = super(Register_EmpregadorForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.user_type = "Empregador"
        if commit:
            user.save()
            empregado = Empregador()
            empregado.user_id = user.id
            empregado.cnpj = self.cleaned_data['cnpj']
            empregado.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']

        
class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='Email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(
            'Nenhum usuário encontrado com este e-mail'
        )

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'password_reset_mail.html'
        subject = 'Criar nova senha no Portal CIESGA'
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template_name, context, [user.email])


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name']

class UserForm(forms.ModelForm):
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'name', 'user_type','is_active', 'is_staff']


