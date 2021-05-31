from django.db import models

# Create your models here.
class Alumno(models.Model):
    cui = models.TextField()
    nombres = models.TextField()
    apellidos = models.TextField()
    escuela = models.TextField()
