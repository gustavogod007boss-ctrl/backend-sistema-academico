from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    carrera = models.ForeignKey(
        Carrera, related_name='alumnos', on_delete=models.CASCADE
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=10, unique=True)
    creditos = models.IntegerField()
    carrera = models.ForeignKey(
        Carrera, related_name='materias', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    alumno = models.ForeignKey(
        Alumno, related_name='inscripciones', on_delete=models.CASCADE
    )
    materia = models.ForeignKey(
        Materia, related_name='inscripciones', on_delete=models.CASCADE
    )
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    calificacion = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('alumno', 'materia')

    def __str__(self):
        return f"{self.alumno} - {self.materia}"
# Create your models here.
