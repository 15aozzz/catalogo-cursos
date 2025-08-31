from django.test import TestCase
from .models import Curso

class CursoTestCase(TestCase):
    def setUp(self):
        # Creamos un curso de prueba
        self.curso = Curso.objects.create(
            curso="Python Básico",
            duracion="2 semanas",
            plataforma="Udemy",
            dificultad="Fácil"
        )

    def test_curso_creado_correctamente(self):
        """
        Verifica que el curso se haya creado con los datos correctos
        """
        self.assertEqual(self.curso.curso, "Python Básico")
        self.assertEqual(self.curso.duracion, "2 semanas")
        self.assertEqual(self.curso.plataforma, "Udemy")
        self.assertEqual(self.curso.dificultad, "Fácil")

    def test_eliminar_curso(self):
        """
        Verifica que un curso pueda eliminarse correctamente
        """
        id_curso = self.curso.id
        self.curso.delete()
        existe = Curso.objects.filter(id=id_curso).exists()
        self.assertFalse(existe)
