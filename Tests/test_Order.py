import pytest

from Order import Order

# Fixtures https://doc.pytest.org/en/latest/reference/fixtures.html#fixture

@pytest.fixture
def order():
    return Order()

# class TestOrder:
#     def test_
