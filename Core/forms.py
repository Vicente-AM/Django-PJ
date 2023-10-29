from django import forms
from .models import Proyecto
from .models import Autos

class proyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'descripcion')

class AutoForm(forms.ModelForm):
    class Meta:
        model = Autos
        fields = '__all__'