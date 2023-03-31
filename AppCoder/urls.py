
from AppCoder.views import *
from django.urls import path

urlpatterns = [
    path('cursos', cursos, name="AppCoderCursos"),
    path('estudiantes', estudiantes, name="AppCoderEstudiantes"),
    path('profesores', profesores, name= "AppCoderProfesores"),
    path('curso/<nombre>/<camada>', crear_curso, name="AppCoderCreaCurso"),
    ]