import unittest

import pricing
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", pricing.NEW_RELEASE)
        self.regular_movie = Movie("Air",pricing.REGULAR)
        self.childrens_movie = Movie("Frozen",pricing.CHILDREN)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", pricing.REGULAR)
        self.assertEqual("Air", m.get_title())

    @unittest.skip("add this test when you refactor rental price")
    def test_rental_price(self):
        rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 15.0)
        self.fail("TODO add more tests for other movie categories")

    @unittest.skip("add this test of rental points when you add it to Rental")
    def test_rental_points(self):
        self.fail("add this test of frequent renter points")

    def test_get_price_regular(self):
        movie = Movie("Regular Movie", pricing.REGULAR)
        rental = Rental(movie, 3, Rental.REGULAR)
        self.assertAlmostEqual(rental.get_price(), 3.5)

    def test_get_price_childrens(self):
        movie = Movie("Children's Movie", pricing.CHILDREN)
        rental = Rental(movie, 4, Rental.CHILDRENS)
        self.assertAlmostEqual(rental.get_price(), 3.0)

    def test_rental_points_regular(self):
        movie = Movie("Regular Movie", pricing.REGULAR)
        rental = Rental(movie, 3, Rental.REGULAR)
        self.assertEqual(rental.rental_points(), 1)

    def test_rental_points_childrens(self):
        movie = Movie("Children's Movie", pricing.CHILDREN)
        rental = Rental(movie, 4, Rental.CHILDRENS)
        self.assertEqual(rental.rental_points(), 1)
