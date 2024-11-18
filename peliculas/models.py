from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200, unique=True)  # Título de la película
    descripcion = models.TextField()  # Descripción de la película
    director = models.CharField(max_length=100)  # Nombre del director
    elenco = models.TextField()  # Miembros del elenco, separado por comas
    idiomas = models.CharField(max_length=200)  # Idiomas disponibles, separado por comas
    cartel = models.ImageField(upload_to='carteles/')  # Imagen del cartel de la película

    def __str__(self):
        return self.titulo
