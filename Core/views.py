from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, "D:\MiProyecto\Core\Templates\core\home.html")

def index(request):
    return render(request, "D:\MiProyecto\Core\Templates\core\index.html")

def catalogo(request):
    return render(request, "D:\MiProyecto\Core\Templates\core\catalogo.html")

def contacto(request):
    return render(request, "D:\MiProyecto\Core\Templates\core\contacto.html")

def nosotros(request):
    return render(request, "D:/MiProyecto/Core/Templates/core/nosotros.html")

#def formulario(request):
#    formulario = proyectoForm()
#    return render(request, "D:\Django-Project\MiProyecto\Templates\core\formulario.html", {'form': formulario})

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/catalogo.html', {'usuarios': usuarios})



