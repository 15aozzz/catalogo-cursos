from django.db import models

class Curso(models.Model):
    curso = models.CharField(max_length=200)

    DURACION_CHOICES = [
        ('1 semana', '1 semana'),
        ('2 semanas', '2 semanas'),
        ('3 semanas', '3 semanas'),
        ('4 semanas', '4 semanas'),
        ('8 horas', '8 horas'),
        ('16 horas', '16 horas'),
        ('24 horas', '24 horas'),
    ]
    duracion = models.CharField(max_length=20, choices=DURACION_CHOICES)

    PLATAFORMA_CHOICES = [
        ('Udemy', 'Udemy'),
        ('Coursera', 'Coursera'),
        ('Platzi', 'Platzi'),
        ('edX', 'edX'),
        ('YouTube', 'YouTube'),
    ]
    plataforma = models.CharField(max_length=50, choices=PLATAFORMA_CHOICES)

    dificultad = models.CharField(
        max_length=20,
        choices=[
            ('Facil', 'Fácil'),
            ('Intermedio', 'Intermedio'),
            ('Avanzado', 'Avanzado')
        ]
    )

    def __str__(self):
        return self.curso
