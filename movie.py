from dataclasses import dataclass, field
from typing import Collection

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
