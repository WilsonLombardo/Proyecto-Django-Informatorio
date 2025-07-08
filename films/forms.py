from django import forms
from .models import Film, Review

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'original_title', 'year', 'director', 
                 'duration', 'genre', 'synopsis', 'poster']
        widgets = {
            'year': forms.NumberInput(attrs={'min': 1888}),
            'duration': forms.NumberInput(attrs={'min': 1}),
            'synopsis': forms.Textarea(attrs={'rows': 4}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'review_text': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'review_text': 'Reseña (opcional)'
        }