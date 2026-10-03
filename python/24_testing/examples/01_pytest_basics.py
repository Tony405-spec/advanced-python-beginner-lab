"""pytest basics: assertions, fixtures, parametrization, exceptions.

Run:
    pytest python/24_testing/examples/01_pytest_basics.py -v

This file is both runnable code AND a valid pytest suite. The `main()`
function at the bottom is only executed when run as a script — pytest
imports the module and calls the test functions directly.
"""

import pytest


# ---------------------------------------------------------------
# Code under test
# ---------------------------------------------------------------

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


class ShoppingCart:
    def __init__(self):
        self._items = {}

    def add(self, name: str, price: float, qty: int = 1) -> None:
        if price < 0:
            raise ValueError(f"price must be non-negative, got {price}")
        self._items[name] = self._items.get(name, 0) + qty

    def total(self) -> float:
        return sum(
            self._price_lookup.get(name, 0) * qty
            for name, qty in self._items.items()
        )

    _price_lookup: dict = {}


# ---------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------

@pytest.fixture
def empty_cart():
    return ShoppingCart()


@pytest.fixture
def cart_with_items():
    cart = ShoppingCart()
    cart._price_lookup = {"apple": 0.5, "bread": 2.0}
    cart.add("apple", 0.5, 3)
    cart.add("bread", 2.0, 1)
    return cart


# ---------------------------------------------------------------
# Basic tests
# ---------------------------------------------------------------

def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)


# ---------------------------------------------------------------
# Parametrized tests
# ---------------------------------------------------------------

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -1, -2),
        (10, -5, 5),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


# ---------------------------------------------------------------
# Exception testing
# ---------------------------------------------------------------

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_divide_by_zero_message():
    with pytest.raises(ZeroDivisionError, match="cannot divide"):
        divide(1, 0)


def test_negative_price_raises():
    with pytest.raises(ValueError, match="non-negative"):
        ShoppingCart().add("item", -1.0)


# ---------------------------------------------------------------
# Fixture tests
# ---------------------------------------------------------------

def test_empty_cart_total(empty_cart):
    assert empty_cart.total() == 0


def test_cart_with_items_total(cart_with_items):
    # 3 * 0.5 + 1 * 2.0 = 3.5
    assert cart_with_items.total() == pytest.approx(3.5)


def test_cart_add_same_item_twice(cart_with_items):
    cart_with_items.add("apple", 0.5, 2)
    # now 5 apples + 1 bread = 5 * 0.5 + 2.0 = 4.5
    assert cart_with_items.total() == pytest.approx(4.5)


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
