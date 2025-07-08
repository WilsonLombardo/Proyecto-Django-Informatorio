from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Film, Review, Watchlist
from .forms import FilmForm, ReviewForm

def home(request):
    latest_films = Film.objects.all().order_by('-created_at')[:10]
    latest_reviews = Review.objects.all().order_by('-created_at')[:5]
    return render(request, 'films/home.html', {
        'latest_films': latest_films,
        'latest_reviews': latest_reviews
    })

def film_detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    reviews = film.reviews.all().order_by('-created_at')
    user_review = None
    in_watchlist = False
    
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
        in_watchlist = Watchlist.objects.filter(user=request.user, film=film).exists()
    
    return render(request, 'films/film_detail.html', {
        'film': film,
        'reviews': reviews,
        'user_review': user_review,
        'in_watchlist': in_watchlist
    })

@login_required
def add_review(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    
    if Review.objects.filter(film=film, user=request.user).exists():
        messages.warning(request, 'Ya has publicado una reseña para esta película.')
        return redirect('film_detail', film_id=film.id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.film = film
            review.user = request.user
            review.save()
            messages.success(request, 'Tu reseña ha sido publicada.')
            return redirect('film_detail', film_id=film.id)
    else:
        form = ReviewForm()
    
    return render(request, 'films/add_review.html', {'form': form, 'film': film})

@login_required
def toggle_watchlist(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    watchlist_item, created = Watchlist.objects.get_or_create(
        user=request.user,
        film=film
    )
    
    if not created:
        watchlist_item.delete()
        messages.success(request, f'"{film.title}" eliminada de tu watchlist.')
    else:
        messages.success(request, f'"{film.title}" agregada a tu watchlist.')
    
    return redirect('film_detail', film_id=film.id)