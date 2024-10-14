import PriceStrategy


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
    
    def __init__(self, title, price_code, price_strategy: PriceStrategy):
        # Initialize a new movie. 
        self.title = title
        self.price_strategy = price_strategy
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_price(self, days: int) -> float:
        """Compute the rental price for this movie."""
        return self.price_strategy.get_price(days)

    def get_rental_points(self, days: int) -> int:
        """Compute frequent renter points for this movie."""
        return self.price_strategy.get_rental_points(days)
