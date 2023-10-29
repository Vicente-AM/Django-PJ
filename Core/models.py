from typing import Any
from django.db import models

# Create your models here.

from django.utils import timezone


class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True)

class Autos(models.Model):
    id = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=100, verbose_name="Marca")
    Modelo = models.CharField(max_length=100, verbose_name="Modelo")
    Imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name="Imagen")
    #nombre = models.CharField(max_length=100)
    #descripcion = models.TextField(verbose_name="Descripción", max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        fila = "Modelo: " + self.Modelo + " - " + "Marca: " + self.Marca
        return fila
    
    def delete(self, using: Any=None, keep_parents: bool=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()