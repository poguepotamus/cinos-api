# pylint: disable=redefined-outer-name,missing-docstring
import pytest

from Drink import Drink


# Fixtures https://doc.pytest.org/en/latest/reference/fixtures.html#fixture
@pytest.fixture
def drink():
    return Drink('sbrite')


class TestDrink:
    def test_get_base(self, drink):
        assert drink.get_base() == 'sbrite'

    def test_flavors(self, drink):
        assert drink.get_flavors() == {}

        # Set flavors should accept a list or set
        drink.set_flavors(['cherry', 'mint'])
        assert drink.get_flavors() == {'cherry', 'mint'}

        drink.set_flavors({'cherry', 'mint', 'lime'})
        assert drink.get_flavors() == {'cherry', 'mint', 'lime'}
        assert drink.get_num_flavors() == 3

        # Testing our flavor addition method
        drink.add_flavor('blueberry')
        assert drink.get_flavors() == {'cherry', 'mint', 'lime', 'blueberry'}
        assert drink.get_num_flavors() == 4

    def test_total(self, drink):
        assert drink.get_total() == 1
