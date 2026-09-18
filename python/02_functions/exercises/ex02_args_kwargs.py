"""Module 02 Exercise 02 — *args and **kwargs (⭐⭐ intermediate).

Fill in each function so the tests in
tests/test_ex02_args_kwargs.py pass.
"""

from typing import Any


def total(*numbers: float) -> float:
    """Return the sum of all positional arguments.

    total() == 0
    total(1, 2, 3) == 6
    """
    raise NotImplementedError


def merge_dicts(*dicts: dict) -> dict:
    """Merge all dictionaries left-to-right.

    Later keys override earlier keys.
    merge_dicts({"a": 1}, {"b": 2}, {"a": 3}) == {"a": 3, "b": 2}
    """
    raise NotImplementedError


def describe(**fields: Any) -> str:
    """Return a string listing key=value pairs sorted by key.

    describe(b=2, a=1, c=3) == "a=1, b=2, c=3"
    """
    raise NotImplementedError
