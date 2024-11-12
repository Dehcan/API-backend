from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.decorators import login_required

def listar_libros(request):
    libros = Libro.objects.all().order_by('-fecha_publicacion')
    return render(request, 'libros/listar_libros.html', {'libros': libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})

@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            return redirect('libros:detalle_libro', pk=libro.pk)
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libros:detalle_libro', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form})
