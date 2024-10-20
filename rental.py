from movie import Movie
import logging
from pricing import NEW_RELEASE, REGULAR, CHILDREN

class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    NEW_RELEASE = NEW_RELEASE
    REGULAR = REGULAR
    CHILDRENS = CHILDREN

    def __init__(self, movie, days_rented, price_code):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_price(self) -> float:
        return self.price_code.get_price(self.days_rented)

    def rental_points(self) -> int:
        return self.price_code.get_rental_points(self.days_rented)

