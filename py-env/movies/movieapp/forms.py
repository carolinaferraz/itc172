from django import forms
from .models import Theater, Movie

class TheaterForm(forms.ModelForm):
    class Meta:
        model=Theater
        fields='__all__'

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'