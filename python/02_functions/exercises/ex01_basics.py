"""Module 02 Exercise 01 — Function basics (⭐ beginner).

Fill in each function so the tests in
tests/test_ex01_basics.py pass.

Run tests with:
    pytest python/02_functions/tests/test_ex01_basics.py -v
"""

from typing import Callable


def add(a: int, b: int) -> int:
    """Return a + b."""
    raise NotImplementedError


def apply(func: Callable[[int], int], value: int) -> int:
    """Return func(value)."""
    raise NotImplementedError


def apply_n(func: Callable[[int], int], value: int, n: int) -> int:
    """Apply func to value n times.

    Example: apply_n(lambda x: x + 1, 0, 3) == 3
    """
    raise NotImplementedError


def make_greeting(prefix: str) -> Callable[[str], str]:
    """Return a function that greets a name with the given prefix.

    Example:
        hello = make_greeting("Hello")
        hello("Ada") == "Hello, Ada"
    """
    raise NotImplementedError
