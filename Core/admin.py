from django.contrib import admin
from .models import Proyecto
from .models import Usuario

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Usuario)
