from django.urls import path
from .views import *



urlpatterns = [
    path('agregar-curso/<nombre>/<comision>', curso),
    path('lista-curso/', listar_curso),
    path('', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]
