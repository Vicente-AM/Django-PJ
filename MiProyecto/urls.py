"""MiProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from Core import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"), #este deberia ser index
    path('nosotros.html', views.nosotros, name="nosotros"),
    path('contacto.html', views.contacto, name="contacto"),
    path('catalogo.html', views.catalogo, name="catalogo"),
#    path('', views.formulario, name="formulario"),
    path('index.html', views.index, name="index"),
    path('entrada.html', views.entrada, name="entrada"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
