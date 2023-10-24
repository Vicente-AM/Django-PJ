from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, "D:\Django-Project\Core\Templates\Core\home.html")

def index(request):
    return render(request, "D:\Django-Project\Core\Templates\Core\index.html")

def nosotros(request):
    return render(request, "/Core/Templates/Core/nosotros.html")

def catalogo(request):
    return render(request, "D:\Django-Project\Core\Templates\Core\catalogo.html")

def formulario(request):
    formulario = proyectoForm()
    return render(request, "D:\Django-Project\Core\Templates\Core\formulario.html", {'form': formulario})

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/catalogo.html', {'usuarios': usuarios})



