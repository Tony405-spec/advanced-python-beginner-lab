"""Tests for Module 24 Exercise 01 — the reference solution.

Run:
    pytest python/24_testing/tests/test_ex01_writing_tests.py -v
"""

import importlib.util
import sys
from pathlib import Path

import pytest


def _load_exercise_module():
    path = (
        Path(__file__).resolve().parents[1]
        / "exercises"
        / "ex01_writing_tests.py"
    )
    spec = importlib.util.spec_from_file_location("ex01_writing_tests", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["ex01_writing_tests"] = module
    spec.loader.exec_module(module)
    return module


ex = _load_exercise_module()


# ---------------------------------------------------------------
# add
# ---------------------------------------------------------------

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, -5, 5),
        (-3, -4, -7),
    ],
)
def test_add(a, b, expected):
    assert ex.add(a, b) == expected


def test_add_is_commutative():
    assert ex.add(7, 3) == ex.add(3, 7)


# ---------------------------------------------------------------
# is_palindrome
# ---------------------------------------------------------------

@pytest.mark.parametrize(
    "text,expected",
    [
        ("racecar", True),
        ("RaceCar", True),
        ("A man a plan a canal Panama", True),
        ("", True),
        ("a", True),
        ("hello", False),
        ("12321", True),
        ("12345", False),
        ("No 'x' in Nixon", True),
        ("Was it a car or a cat I saw?", True),
        ("not a palindrome", False),
    ],
)
def test_is_palindrome(text, expected):
    assert ex.is_palindrome(text) is expected
# ---------------------------------------------------------------
# divide
# ---------------------------------------------------------------

def test_divide_basic():
    assert ex.divide(10, 2) == 5.0


def test_divide_float_result():
    assert ex.divide(1, 3) == pytest.approx(0.3333, rel=1e-4)


def test_divide_negative():
    assert ex.divide(-1, 2) == -0.5


def test_divide_zero_raises():
    with pytest.raises(ZeroDivisionError):
        ex.divide(1, 0)


# ---------------------------------------------------------------
# find_max
# ---------------------------------------------------------------

def test_find_max_ascending():
    assert ex.find_max([1, 2, 3]) == 3


def test_find_max_descending():
    assert ex.find_max([3, 2, 1]) == 3


def test_find_max_single():
    assert ex.find_max([42]) == 42


def test_find_max_negatives():
    assert ex.find_max([-5, -1, -10]) == -1


def test_find_max_empty_raises():
    with pytest.raises(ValueError, match="non-empty"):
        ex.find_max([])


def test_find_max_returns_type():
    assert isinstance(ex.find_max([1, 2, 3]), int)
