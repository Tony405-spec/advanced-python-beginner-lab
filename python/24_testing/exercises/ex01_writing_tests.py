"""Module 24 Exercise 01 — write tests for this code ( beginner).

The functions below are SIMPLE ON PURPOSE. Your job is to write
thorough tests for them in the companion file:

    python/24_testing/tests/test_ex01_writing_tests.py

The tests file currently raises NotImplementedError for each test
function. Fill them in until `pytest` reports all green.

Pay attention to:
    - Normal cases
    - Boundary values (0, 1, negative, empty)
    - Error conditions (invalid inputs)
    - Return types
"""


def add(a: int, b: int) -> int:
    """Add two ints. Accepts any ints (positive, negative, zero)."""
    return a + b


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards.

    Case-insensitive. Ignores spaces, punctuation via str.isalnum().

    Examples:
        is_palindrome("racecar") == True
        is_palindrome("A man a plan a canal Panama") == True
        is_palindrome("hello") == False
        is_palindrome("") == True
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def divide(a: float, b: float) -> float:
    """Return a / b.

    Raises:
        ZeroDivisionError if b == 0.
    """
    return a / b


def find_max(items: list):
    """Return the largest item in a non-empty list.

    Raises:
        ValueError if items is empty.
    """
    if not items:
        raise ValueError("find_max requires a non-empty list")
    return max(items)
