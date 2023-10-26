from django.shortcuts import render
from django.http import HttpResponse
from .models import Autos

# Create your views here.

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, 'index.html')

def entrada(request):
    return render(request, "entrada.html")

def catalogo(request):
    autos = Autos.objects.all()
    return render(request, "catalogo.html", {'autos': autos})

def contacto(request):
    return render(request, "contacto.html")

def nosotros(request):
    return render(request, "nosotros.html")

#def formulario(request):
#    formulario = proyectoForm()
#    return render(request, "D:\Django-Project\MiProyecto\Templates\core\formulario.html", {'form': formulario})

#def usuarios(request):
#    usuarios = Usuario.objects.all()
#    return render(request, 'usuarios/catalogo.html', {'usuarios': usuarios})



