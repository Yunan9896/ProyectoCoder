from django.urls import path
from .views import *



urlpatterns = [
    path('agregar-curso/<nombre>/<comision>', curso),
    path('lista-curso/', listar_curso),
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),
]
