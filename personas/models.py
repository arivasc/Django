from django.db import models

# Create your models here.

class Persona(models.Model):
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    edad = models.PositiveSmallIntegerField()
    donador = models.BooleanField(default=False)
