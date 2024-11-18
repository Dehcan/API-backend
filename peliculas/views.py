from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pelicula
from .forms import PeliculaForm
from django.contrib.auth.decorators import login_required

def listar_peliculas(request):
    peliculas = Pelicula.objects.all().order_by('titulo')  # Ordena por título
    return render(request, 'peliculas/listar_peliculas.html', {'peliculas': peliculas})

def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas/detalle_pelicula.html', {'pelicula': pelicula})

@login_required
def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            pelicula = form.save()
            messages.success(request, 'Película creada exitosamente.')
            return redirect('peliculas:detalle_pelicula', pk=pelicula.pk)
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/crear_pelicula.html', {'form': form})

@login_required
def editar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            messages.success(request, 'Película actualizada exitosamente.')
            return redirect('peliculas:detalle_pelicula', pk=pelicula.pk)
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'peliculas/editar_pelicula.html', {'form': form, 'pelicula': pelicula})

@login_required
def borrar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        pelicula.delete()
        messages.success(request, 'Película eliminada exitosamente.')
        return redirect('peliculas:listar_peliculas')
    return render(request, 'peliculas/borrar_pelicula.html', {'pelicula': pelicula})
