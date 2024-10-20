import unittest

from django.utils.translation.trans_real import catalog

from movie import Movie, MovieCatalog
from pricing import get_price_for_movie, NEW_RELEASE, REGULAR, CHILDREN

class TestPricing(unittest.TestCase):

    def test_regular_price(self):
        catalog_1 = MovieCatalog()
        movie = catalog_1.get_movie("Top Gun: Maverick")
        days = 3
        price = get_price_for_movie(movie, days)
        expected_price = 2.0 + 1.5 * (days - 2)
        self.assertEqual(price, expected_price)

    def test_childrens_price(self):
        catalog_2 = MovieCatalog()
        movie = catalog_2.get_movie("The Legend of Sarila")
        days = 4
        price = get_price_for_movie(movie, days)
        expected_price = 1.5 + 1.5 * (days - 3)
        self.assertEqual(price, expected_price)

    def test_new_release_price(self):
        catalog_3 = MovieCatalog()
        movie = catalog_3.get_movie("Young Woman and the Sea")
        days = 4
        price = get_price_for_movie(movie, days)
        expected_price = 3 * days
        self.assertEqual(price, expected_price)

if __name__ == '__main__':
    unittest.main()
