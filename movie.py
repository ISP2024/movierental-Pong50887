from pricing import NEW_RELEASE, REGULAR, CHILDREN


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    NEW_RELEASE = NEW_RELEASE
    REGULAR = REGULAR
    CHILDRENS = CHILDREN

    def __init__(self, title, price_code):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    # def get_price(self, days):
    #     # get the movie prices
    #     return self.price_code.get_price(days)
    #
    # def get_rental_points(self, days):
    #     # get the movie rental points
    #     return self.price_code.get_rental_points(days)

    def __str__(self):
        return self.title
