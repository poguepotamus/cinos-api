import pytest

from API.Order import Order

# Fixtures https://doc.pytest.org/en/latest/reference/fixtures.html#fixture

@pytest.fixture
def test_order(test_drink_size):
    return Order()

# class TestOrder:
#     def test_
