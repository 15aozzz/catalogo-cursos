"""
URL configuration for crud_cursos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cursos import views  # Importa todas las vistas que creaste en la app cursos

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),

    # Página principal -> aquí redirigimos al formulario de registro
    path('', views.registrar_curso, name='inicio'),

    # Ruta para registrar un curso (muestra y procesa el formulario)
    path('registrar/', views.registrar_curso, name='registrar_curso'),

    # Ruta para listar todos los cursos registrados
    path('cursos/', views.listar_cursos, name='listar_cursos'),

    # Ruta para editar un curso (se pasa el ID en la URL)
    path('editar/<int:id>/', views.editar_curso, name='editar_curso'),

    # Ruta para eliminar un curso (se pasa el ID en la URL)
    path('eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
]