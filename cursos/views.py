from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso

# 👉 Vista para registrar un curso
def registrar_curso(request):
    if request.method == 'POST':  # Si el usuario envía el formulario
        curso = request.POST['curso']
        duracion = request.POST['duracion']
        plataforma = request.POST['plataforma']
        dificultad = request.POST['dificultad']

        # Guardamos en la base de datos
        Curso.objects.create(
            curso=curso,
            duracion=duracion,
            plataforma=plataforma,
            dificultad=dificultad
        )

        # Se envía un mensaje de éxito al template
        return render(request, 'cursos/registrar_curso.html', {
            'mensaje': 'Curso registrado con éxito'
        })

    # Si es GET, mostramos solo el formulario
    return render(request, 'cursos/registrar_curso.html')


# 👉 Vista para mostrar todos los cursos en una tabla
def listar_cursos(request):
    cursos = Curso.objects.all()  # Trae todos los cursos de la BD
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})


# 👉 Vista para editar un curso existente
def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)  # Busca el curso por id o lanza error 404

    if request.method == 'POST':  # Si se envió el formulario de edición
        curso.curso = request.POST['curso']
        curso.duracion = request.POST['duracion']
        curso.plataforma = request.POST['plataforma']
        curso.dificultad = request.POST['dificultad']
        curso.save()  # Guarda los cambios
        return redirect('listar_cursos')  # Redirige a la lista de cursos

    # Si es GET, mostramos el formulario con los datos actuales del curso
    return render(request, 'cursos/editar_curso.html', {'curso': curso})


# 👉 Vista para eliminar un curso
def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)  # Busca el curso
    curso.delete()  # Lo elimina de la BD
    return redirect('listar_cursos')  # Redirige a la lista
