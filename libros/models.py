from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    edicion = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
