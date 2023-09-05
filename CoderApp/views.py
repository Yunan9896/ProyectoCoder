from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Curso
from .forms import CursoFormulario


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

def cursoFormulario(request):
    print('method', request.method)
    print('POST', request.POST)
    
        
    if request == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso = Curso(nombre = data["curso"], comision = data["comision"])
            curso.save()
            return render(request, "inicio.html" )
    else: 
        miFormulario = CursoFormulario()
        return render(request, "cursoFormulario.html" ,{"miFormulario": miFormulario})
    
def busquedaComision(request):
    return render(request, "busquedaComision.html")

def buscar(request: HttpRequest):
    if request.GET["comision"]:
        comision = request.GET["comision"]
        curso = Curso.objects.get(comision=comision) #recupera el curso buscado
        return render(request, "resultadosBusqueda.html", {"curso":curso})
    else:
        return HttpResponse(f"Debe agregar comision")