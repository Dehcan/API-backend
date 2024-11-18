from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.listar_libros, name='listar_libros'),
    path('libro/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('borrar/<int:pk>/', views.borrar_libro, name='borrar_libro'),
]
