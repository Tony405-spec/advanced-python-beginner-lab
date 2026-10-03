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
