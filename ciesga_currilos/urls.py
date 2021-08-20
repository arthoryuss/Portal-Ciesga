"""ciesga_currilos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings	
from django.conf.urls.static import static
from core import urls

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace="core")),
    path('usuario/', include('usuario.urls', namespace="usuario")),
    path('candidato/', include('candidato.urls', namespace="candidato")),
    path('empregador/', include('empregador.urls', namespace="empregador")),
    path('vagas/', include('vagas.urls', namespace="vagas")),
    path('captcha/', include('captcha.urls')),
    
    
    #path('municipios_app/', include('municipios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
