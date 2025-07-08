from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('film/<int:film_id>/', views.film_detail, name='film_detail'),
    path('film/<int:film_id>/review/', views.add_review, name='add_review'),
    path('film/<int:film_id>/watchlist/', views.toggle_watchlist, name='toggle_watchlist'),
]