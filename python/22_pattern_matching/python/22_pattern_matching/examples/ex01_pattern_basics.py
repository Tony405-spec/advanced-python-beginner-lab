"""Module 22 Exercise 01 — pattern matching basics ( beginner).

Fill in each function so that the corresponding tests pass.

Run tests with:
    pytest python/22_pattern_matching/tests/test_ex01_pattern_basics.py -v
"""

from typing import Any


def http_class(code: int) -> str:
    """Return the HTTP class name for a status code.

    Rules:
        100–199 -> "informational"
        200–299 -> "success"
        300–399 -> "redirect"
        400–499 -> "client error"
        500–599 -> "server error"
        anything else -> "invalid"

    Use match/case with guards.
    """
    raise NotImplementedError


def parse_date_like(value: Any) -> tuple[int, int, int] | None:
    """Parse common date shapes into (year, month, day).

    Accepted shapes:
        (2024, 1, 15)         -> (2024, 1, 15)
        [2024, 1, 15]         -> (2024, 1, 15)
        {"y": 2024, "m": 1, "d": 15} -> (2024, 1, 15)

    Anything else -> None

    Use match/case with sequence, mapping, and class patterns.
    """
    raise NotImplementedError


def describe_shape(shape: Any) -> str:
    """Describe a shape-like object.

    Accepts:
        int or float  -> "number: <value>"
        str           -> "text: <value>"
        list or tuple -> "sequence of <n>"
        dict          -> "mapping with <n> keys"
        anything else -> "unknown"
    """
    raise NotImplementedError
