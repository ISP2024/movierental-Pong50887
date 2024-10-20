import csv
import logging
from collections import defaultdict
from typing import Collection
from typing import Optional, List
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genre: Collection[str] = field(default_factory=list)

    def is_genre(self, genre_name: str) -> bool:
        return genre_name.lower() in (genre.lower() for genre in self.genre)

    def __str__(self):
        return f"{self.title} ({self.year})"


class MovieCatalog:
    """Singleton class to manage a collection of movies."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.movies = []
            cls._instance._load_movies()
        return cls._instance

    def _load_movies(self):
        """Load movies from the CSV file."""
        with open('movies.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for line_number, row in enumerate(reader, start=1):
                if not row or row[0].startswith('#'):
                    continue
                if len(row) < 4:
                    logging.error(f"Line {line_number}: Unrecognized format \"{','.join(row)}\"")
                    continue

                try:
                    movie_id, title, year, genres = row
                    year = int(year)
                    genre_list = genres.split('|')
                    movie = Movie(title=title, year=year, genre=genre_list)
                    self.movies.append(movie)
                except (ValueError, TypeError) as e:
                    logging.error(f"Line {line_number}: Unrecognized format \"{','.join(row)}\"")

    def get_movie(self, title: str, year: int = None) -> Movie:
        """Get a movie by title and optional year."""
        for movie in self.movies:
            if movie.title.lower() == title.lower() and (year is None or movie.year == year):
                return movie
        return None


if __name__ == "__main__":
    # Get the Singleton Movie Catalog
    catalog = MovieCatalog()
    # Get the first movie named 'Mulan'
    movie_1 = catalog.get_movie("Mulan")
    if not movie_1:
        print("Sorry, couldn't find that movie.")
    print(movie_1)

    movie_2 = catalog.get_movie("No Time to Die")
    if not movie_2:
        print("Sorry, couldn't find that movie.")
    print(movie_2)