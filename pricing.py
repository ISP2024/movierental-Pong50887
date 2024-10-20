from abc import ABC, abstractmethod
from datetime import datetime

from movie import Movie


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instance = None

    @classmethod
    def __new__(cls, *args):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing and point earning rules for New Release movies."""

    def get_rental_points(self, days):
        """Renter gets 1 point per day rented."""
        return days

    def get_price(self, days):
        """The rental price for $3 per day."""
        return 3 * days


class RegularPrice(PriceStrategy):
    """Pricing and point earning rules for Regular movies."""

    def get_rental_points(self, days):
        """Regular movie rentals get only 1 point."""
        return 1

    def get_price(self, days):
        """The first two days cost $2 total, then $1.50 is added per additional day."""
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount


class ChildrensPrice(PriceStrategy):
    """Pricing and point earning rules for Children movies."""

    def get_rental_points(self, days):
        """Children movie rentals get only 1 point."""
        return 1

    def get_price(self, days):
        """The first three days cost $1.50 total, then $1.50 is added per additional day."""
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount


NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()

def price_code_for_movie(movie: Movie) -> PriceStrategy:
    """Determine the price code for a given movie."""
    current_year = datetime.now().year

    if movie.year == current_year:
        return NEW_RELEASE
    elif any(genre.lower() == "children" for genre in movie.genre):
        return CHILDREN
    else:
        return REGULAR

def get_price_for_movie(movie: Movie, days: int) -> float:
    price_strategy = price_code_for_movie(movie)
    return price_strategy.get_price(days)