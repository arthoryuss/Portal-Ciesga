from django.contrib import admin
from usuario.models import *
from candidato.models import *
from usuario.forms import UserAdminCreationForm, UserForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from candidato.models import Experiencia, Formacao, Idioma, Candidato


class UserAdmin(BaseUserAdmin):

	add_form = UserAdminCreationForm
	add_fieldsets = (
		(None, {
			'fields': ('username', 'name', 'email', 'user_type','password1', 'password2')
		}),
	)
	form = UserForm
	fieldsets = (
		(None, {
			'fields': ('username', 'email', 'user_type')
		}),
		('Informações Básicas', {
			'fields': ('name',)
		}),
		(
			'Permissões', {
				'fields': (
					'is_active', 'is_staff', 'is_superuser', 'groups',
					'user_permissions'
				)
			}
		),
	)
		
	list_display = ['username', 'name', 'email', 'user_type', 'is_active', 'is_staff', 'date_joined']



admin.site.register(User,UserAdmin)


