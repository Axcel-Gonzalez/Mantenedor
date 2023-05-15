from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id, self.nombre

class Personas(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha = models.DateField()
    carrera = models.ForeignKey(Carrera, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre, self.apellido