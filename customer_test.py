import re
import unittest

from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 2023, ["Action", "Adventure"])
        self.regular_movie = Movie("CitizenFour", 2014, ["Documentary"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Children"])

    @unittest.skip("No convenient way to test")
    def test_billing(self):
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("5.00", matches[1])

    def test_get_total_charge(self):
        """Test the total charge calculation for multiple rentals."""
        # Add multiple rentals
        self.c.add_rental(Rental(self.new_movie, 4))  # New Release
        self.c.add_rental(Rental(self.regular_movie, 3))  # Regular
        self.c.add_rental(Rental(self.childrens_movie, 4))  # Children's

        # Check the total charge
        total_charge = self.c.get_total_amount()
        self.assertAlmostEqual(total_charge, 11.5, places=2)  # Ensure this value matches your pricing rules

    def test_get_total_points(self):
        """Test the total points calculation for multiple rentals."""
        # Add multiple rentals
        self.c.add_rental(Rental(self.new_movie, 4))  # New Release
        self.c.add_rental(Rental(self.regular_movie, 3))  # Regular
        self.c.add_rental(Rental(self.childrens_movie, 4))  # Children's

        # Check the total renter points
        total_renter_points = self.c.get_total_renter_points()
        self.assertEqual(total_renter_points, 3)  # Ensure this value matches your points logic

if __name__ == '__main__':
    unittest.main()