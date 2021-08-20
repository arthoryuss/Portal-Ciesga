from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name='usuario'

urlpatterns = [
    path("password_reset", views.password_reset, name='password_reset'),
    path('confirmar-nova-senha/<key>', views.password_reset_confirm, 
        name='password_reset_confirm'),
    path('editar-senha/', views.edit_password,  name='edit_password'),
    path('login/', LoginView.as_view(template_name = 'login.html'), 
    	 name='login'),
    path('logout/', LogoutView.as_view(next_page= 'core:home'), 
    	 name='logout'),
    path('cadastre-se_candidato/', views.register, name='register'),
    path('cadastre-se_empregador/', views.register_empregador, name='register_empregador'),
    path('painel/', views.dashboard, name='dashboard'),
    path('teste/', views.choice_register, name='choice_register'),
]

