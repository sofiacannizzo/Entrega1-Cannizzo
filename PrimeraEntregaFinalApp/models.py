from configparser import MissingSectionHeaderError
from django.db import models
from django.forms import EmailField, URLField

# Create your models here.
class Inicio(models.Model):
    bievenida = models.CharField(max_length=100)

class Socio(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    deportes = models.CharField(max_length=200)
    email = models.EmailField()

class Deporte(models.Model):
    deporte = models.CharField(max_length=30)
    profesor = models.CharField(max_length=70)
    horario = models.CharField(max_length=60, default="Sin horario")

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    deporte = models.CharField(max_length=30)
    email = models.EmailField()

class Administrador(models.Model):
    puesto = models.CharField(max_length=100)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()