from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Autos
from .forms import AutoForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, 'index.html')

def entrada(request):
    return render(request, "entrada.html")

def crear(request):
    formulario = AutoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('catalogo.html')
    return render(request, "crear.html", {'formulario': formulario})

def formulario(request):
    return render(request, "formulario.html")

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



