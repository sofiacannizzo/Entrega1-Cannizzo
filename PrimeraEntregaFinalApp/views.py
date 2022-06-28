from ast import If
from django.shortcuts import redirect, render
from django.http import HttpResponse
from PrimeraEntregaFinalApp.models import *
from django.template import Template, Context
from .forms import *

# Create your views here.
def socios(request):
    socios = Socio.objects.all()
    print(socios)
    return render(request, "PrimeraEntregaFinalApp/socios.html", {"socios": socios})

def deportes(request):
    deportes = Deporte.objects.all()
    print(deportes)
    return render(request, "PrimeraEntregaFinalApp/deportes.html", {"deportes": deportes})

def profesores(request):
    profesores = Profesor.objects.all()
    print(profesores)
    return render(request, "PrimeraEntregaFinalApp/profesores.html", {"profesores": profesores})

def administracion(request):
    administracion = Administrador.objects.all()
    print(administracion)
    return render(request, "PrimeraEntregaFinalApp/administracion.html", {"administracion": administracion})

def inicio(request):
    inicio = Inicio.objects.all()
    print(inicio)
    return render(request, "PrimeraEntregaFinalApp/index.html", {"inicio": inicio})

def base(request):
    return render(request, "PrimeraEntregaFinalApp/base.html", {})

def crear_profesor(request):
    if request.method == "POST":
        formulario = NuevoProfesor(request.POST)
        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data
            profesor = Profesor(nombre=info["nombre"],apellido=info["apellido"],deporte=info["deporte"],email=info["email"])
            profesor.save()
            return redirect("profesores")

    else:
        formulario = NuevoProfesor()
        return render(request,"PrimeraEntregaFinalApp/form_profesores.html",{"form":formulario})
    
def crear_administrador(request):
    if request.method == "POST":
        formulario = NuevoAdministrador(request.POST)
        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data
            administracion = Administrador(puesto=info["puesto"],nombre=info["nombre"],apellido=info["apellido"],email=info["email"])
            administracion.save()
            return redirect("administracion")

    else:
        formulario = NuevoAdministrador()
        return render(request,"PrimeraEntregaFinalApp/form_administracion.html",{"form":formulario})
    
def crear_deporte(request):
    if request.method == "POST":
        formulario = NuevoDeporte(request.POST)
        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data
            deporte = Deporte(deporte=info["deporte"],profesor=info["profesor"],horario=info["horario"])
            deporte.save()
            return redirect("deportes")

    else:
        formulario = NuevoDeporte()
        return render(request,"PrimeraEntregaFinalApp/form_deportes.html",{"form":formulario})
    
def crear_socio(request):
    if request.method == "POST":
        formulario = NuevoSocio(request.POST)
        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data
            socios = Socio(nombre=info["nombre"],apellido=info["apellido"],deportes=info["deportes"],edad=info["edad"],email=info["email"])
            socios.save()
            return redirect("socios")

    else:
        formulario = NuevoSocio()
        return render(request,"PrimeraEntregaFinalApp/form_socios.html",{"form":formulario})
    
def buscar_apellido_socio(request):
    if request.method == "POST":
        apellido = request.POST["apellido"]
        apellido = Socio.objects.filter(apellido__icontains=apellido)
        return render(request, "PrimeraEntregaFinalApp/buscar_apellido_socio.html", {"apellido":apellido})
    else:
        apellido = []
        return render(request, "PrimeraEntregaFinalApp/buscar_apellido_socio.html", {"apellido":apellido})
