import unittest
from movie import Movie
from pricing import get_price_for_movie

class TestPricing(unittest.TestCase):

    def setUp(self):
        self.new_release_movie = Movie(title="Young Woman and the Sea", year=2024, genre=["Drama", "Adventure"])
        self.regular_movie = Movie(title="Top Gun: Maverick", year=2022, genre=["Action"])
        self.childrens_movie = Movie(title="The Legend of Sarila", year=2013, genre=["Animation", "Children"])

    def test_regular_price(self):
        days = 3
        price = get_price_for_movie(self.regular_movie, days)
        expected_price = 2.0 + 1.5 * (days - 2)
        self.assertEqual(price, expected_price)

    def test_childrens_price(self):
        days = 4
        price = get_price_for_movie(self.childrens_movie, days)
        expected_price = 1.5 + 1.5 * (days - 3)
        self.assertEqual(price, expected_price)

    def test_new_release_price(self):
        days = 4
        price = get_price_for_movie(self.new_release_movie, days)
        expected_price = 3 * days
        self.assertEqual(price, expected_price)

if __name__ == '__main__':
    unittest.main()
