import unittest

from rental import Rental
from movie import Movie



class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2023, ["Action", "Adventure"])
        self.regular_movie = Movie("Air", 2023, ["Drama"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Children"])

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ["Drama"])
        self.assertEqual("Air", m.title)

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)

        rental = Rental(self.regular_movie, 3)
        self.assertAlmostEqual(rental.get_price(), 3.5)

        rental = Rental(self.childrens_movie, 4)
        self.assertAlmostEqual(rental.get_price(), 3.0)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.rental_points(), 1)

        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.rental_points(), 1)

        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.rental_points(), 1)


if __name__ == '__main__':
    unittest.main()
