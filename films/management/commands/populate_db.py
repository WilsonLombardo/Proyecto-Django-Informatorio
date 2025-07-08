from django.core.management.base import BaseCommand
from films.models import Film

class Command(BaseCommand):
    help = 'Popula la base de datos con películas de ejemplo'

    def handle(self, *args, **options):
        films_data = [
            {
                'title': 'El Padrino',
                'year': 1972,
                'director': 'Francis Ford Coppola',
                'duration': 175,
                'genre': 'Drama',
                'synopsis': 'El patriarca de una familia criminal transfiere el control a su hijo menor.'
            },
            {
                'title': 'El Caballero Oscuro',
                'year': 2008,
                'director': 'Christopher Nolan',
                'duration': 152,
                'genre': 'Acción',
                'synopsis': 'Batman se enfrenta al Joker en Gotham City.'
            },
            {
                'title': 'Parásitos',
                'year': 2019,
                'director': 'Bong Joon-ho',
                'duration': 132,
                'genre': 'Thriller',
                'synopsis': 'Una familia pobre se infiltra en un hogar adinerado.'
            }
        ]

        for film_data in films_data:
            Film.objects.get_or_create(**film_data)
            self.stdout.write(self.style.SUCCESS(f'Película creada: {film_data["title"]}'))

        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada exitosamente!'))