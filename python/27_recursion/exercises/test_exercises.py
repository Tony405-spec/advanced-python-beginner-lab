import pytest
from exercises.ex01_recursion import recursive_sum, recursive_reverse

def test_recursive_sum():
    assert recursive_sum([]) == 0
    assert recursive_sum([1, 2, 3, 4]) == 10

def test_recursive_reverse():
    assert recursive_reverse("hello") == "olleh"
    assert recursive_reverse("a") == "a"
