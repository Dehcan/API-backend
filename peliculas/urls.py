from django.urls import path
from . import views

app_name = 'peliculas'

urlpatterns = [
    path('', views.listar_peliculas, name='listar_peliculas'),
    path('pelicula/<int:pk>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('crear/', views.crear_pelicula, name='crear_pelicula'),
    path('editar/<int:pk>/', views.editar_pelicula, name='editar_pelicula'),
    path('borrar/<int:pk>/', views.borrar_pelicula, name='borrar_pelicula'),
]