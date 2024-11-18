from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'descripcion', 'edicion', 'fecha_publicacion', 'autor', 'isbn', 'idioma', 'portada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'edicion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'idioma': forms.TextInput(attrs={'class': 'form-control'}),
            'portada': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
