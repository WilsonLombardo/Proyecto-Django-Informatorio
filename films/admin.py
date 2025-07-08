from django.contrib import admin
from .models import Film, Review, Watchlist

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'genre')
    search_fields = ('title', 'director')
    list_filter = ('year', 'genre')

admin.site.register(Film, FilmAdmin)
admin.site.register(Review)
admin.site.register(Watchlist)