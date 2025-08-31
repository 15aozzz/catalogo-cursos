from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_curso, name='registrar_curso'),  # Formulario de registro
    path('listar/', views.listar_cursos, name='listar_cursos'),  # Listado de cursos
    path('editar/<int:id>/', views.editar_curso, name='editar_curso'),  # Editar curso por id
    path('eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),  # Eliminar curso por id
]
