from django.shortcuts import render
from .models import Curso

def registrar_curso(request):
    mensaje = ""
    if request.method == "POST":
        curso = request.POST['curso']
        duracion = request.POST['duracion']
        plataforma = request.POST['plataforma']
        dificultad = request.POST['dificultad']

        # Crear el curso en la base de datos
        Curso.objects.create(
            curso=curso,
            duracion=duracion,
            plataforma=plataforma,
            dificultad=dificultad
        )

        mensaje = "Curso registrado correctamente"

    return render(request, "cursos/registrar_curso.html", {"mensaje": mensaje})