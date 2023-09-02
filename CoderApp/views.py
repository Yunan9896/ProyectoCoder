from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def curso (request, nombre, comision):
    curso = Curso(nombre = nombre, comision = comision)
    curso.save()
    return HttpResponse(f"""<p> Curso: {curso.nombre} - {curso.comision} creado con exito!!""")

def listar_curso(request):
    lista = Curso.objects.all()
    return render(request, "lista_curso.html", {"lista_curso": lista})

def inicio(request):
    return render(request, "inicio.html")

def cursos(request):
    return render(request, "cursos.html")

def profesores(request):
    return render(request, "profesores.html")

def estudiantes(request):
    return render(request, "estudiantes.html")

def entregables(request):
    return render(request, "entregables.html")