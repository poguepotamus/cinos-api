# pylint: disable=redefined-outer-name,missing-docstring
import pytest

from API.Drink import Drink


# Fixtures https://doc.pytest.org/en/latest/reference/fixtures.html#fixture
@pytest.fixture
def drink():
    return Drink('sbrite', 'small')



@pytest.fixture
def test_drink_size():
    return [
        Drink('sbrite', size='small'),
        Drink('hill fog', 'LARGE', ['cherry', 'strawberry']),
        Drink('pokeacola', 'medium', flavors=['lemon', 'mint', 'lime']),
    ]


class TestDrink:
    def test_drink_constr(self):
        with pytest.raises(Exception):
            Drink('water', size='super')

        for size in ['small', 'medium', 'large', 'mega']:
            Drink('water', size=size)

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

    def test_total(self, test_drink_size):
        results = [1.50, 2.35, 2.10]

        """
        Edge cases
        Hard-code values
        reliability, un-functionality, accuracy
        """

        for pos, drink in enumerate(test_drink_size):
            assert drink.get_total() == results[pos]



