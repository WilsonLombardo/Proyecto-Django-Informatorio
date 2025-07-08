from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Film(models.Model):
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200, blank=True, null=True)
    year = models.PositiveIntegerField()
    director = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duración en minutos")
    genre = models.CharField(max_length=100)
    synopsis = models.TextField()
    poster = models.ImageField(upload_to='films/posters/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} ({self.year})"
    
    class Meta:
        ordering = ['-created_at']

class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review_text = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked_reviews', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.film.title} ({self.rating}/5)"
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['film', 'user']

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlists')
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'film']
        ordering = ['-added_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.film.title}"