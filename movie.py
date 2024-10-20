import pricing


class Movie:
    """
    A movie available for rent.
    """
    
    def __init__(self, title, price_strategy: pricing):
        # Initialize a new movie. 
        self.title = title
        self.price_strategy = price_strategy
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title
