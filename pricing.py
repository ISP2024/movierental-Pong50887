from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    @abstractmethod
    def get_price(self, days_rented: int) -> float:
        pass

    @abstractmethod
    def get_rental_points(self, days_rented: int) -> int:
        pass


class RegularPrice(PriceStrategy):
    """Price strategy for regular movies."""

    def get_price(self, days_rented: int) -> float:
        amount = 2.0
        if days_rented > 2:
            amount += 1.5 * (days_rented - 2)
        return amount

    def get_rental_points(self, days_rented: int) -> int:
        return 1


class ChildrensPrice(PriceStrategy):
    """Price strategy for children's movies."""

    def get_price(self, days_rented: int) -> float:
        amount = 1.5
        if days_rented > 3:
            amount += 1.5 * (days_rented - 3)
        return amount

    def get_rental_points(self, days_rented: int) -> int:
        return 1


class NewRelease(PriceStrategy):
    """Price strategy for new release movies."""

    def get_price(self, days_rented: int) -> float:
        return 3 * days_rented

    def get_rental_points(self, days_rented: int) -> int:
        return days_rented


NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()
