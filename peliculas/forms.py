from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'director', 'elenco', 'idiomas', 'cartel']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'elenco': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separe los nombres con comas'}),
            'idiomas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Separe los idiomas con comas'}),
            'cartel': forms.FileInput(attrs={'class': 'form-control'}),
        }
