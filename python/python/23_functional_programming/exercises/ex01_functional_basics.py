"""Module 23 Exercise 01 — functional programming basics.

Fill in each function so the tests pass.

Run tests with:
    pytest python/23_functional_programming/tests/test_ex01_functional_basics.py -v
"""

from typing import Callable, Iterable


def apply_all(funcs: Iterable[Callable], value):
    """Apply each function in order; return the final value.

    apply_all([], 5) == 5
    apply_all([lambda x: x + 1, lambda x: x * 2], 3) == 8
    """
    raise NotImplementedError


def keep_where(predicate: Callable, items: list):
    """Return items where predicate(item) is True.

    Must use filter() internally (not a comprehension).
    """
    raise NotImplementedError


def transform(items: list, func: Callable) -> list:
    """Return [func(x) for x in items].

    Must use map() internally.
    """
    raise NotImplementedError


def fold_sum(nums: list) -> int | float:
    """Sum a list using functools.reduce().

    fold_sum([]) == 0
    fold_sum([1, 2, 3]) == 6
    """
    raise NotImplementedError
def compose(*funcs: Callable) -> Callable:
    """Return a single function that applies funcs right-to-left.

    compose(f, g, h)(x) == f(g(h(x)))
    compose()(x) == x
    """
    raise NotImplementedError


def curry_add(a: int) -> Callable[[int], int]:
    """Return a function that adds a to its argument.

    curry_add(3)(4) == 7
    """
    raise NotImplementedError


def unique_ordered(items: list) -> list:
    """Return unique items, preserving first-seen order.

    Use only functional tools (no set literal for order, but sets allowed
    internally with an accumulator). Prefer reduce.
    """
    raise NotImplementedError


def pairwise(iterable: Iterable):
    """Yield consecutive (a, b) pairs from iterable.

    list(pairwise([1, 2, 3, 4])) == [(1, 2), (2, 3), (3, 4)]
    list(pairwise([1])) == []
    """
    raise NotImplementedError
