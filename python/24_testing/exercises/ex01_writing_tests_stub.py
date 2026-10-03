"""Stub tests to fill in for Module 24 Exercise 01.

Once the real tests exist in tests/test_ex01_writing_tests.py and
pass, this stub can be deleted. Until then, it documents what the
tests SHOULD cover.

This file intentionally contains no runnable tests — everything is
commented to show the intended coverage.
"""

# --- add(a, b) ---
# - add(2, 3) == 5
# - add(0, 0) == 0
# - add(-1, 1) == 0
# - add(10, -5) == 5
# - property: add(a, b) == add(b, a)

# --- is_palindrome(text) ---
# - is_palindrome("racecar") is True
# - is_palindrome("RaceCar") is True (case-insensitive)
# - is_palindrome("A man a plan a canal Panama") is True
# - is_palindrome("") is True (empty is trivially palindromic)
# - is_palindrome("hello") is False
# - is_palindrome("12321") is True
# - is_palindrome("12345") is False

# --- divide(a, b) ---
# - divide(10, 2) == 5.0
# - divide(1, 3) == pytest.approx(0.3333, rel=1e-4)
# - divide(-1, 2) == -0.5
# - pytest.raises(ZeroDivisionError) when b == 0

# --- find_max(items) ---
# - find_max([1, 2, 3]) == 3
# - find_max([3, 2, 1]) == 3
# - find_max([42]) == 42
# - find_max([-5, -1, -10]) == -1
# - pytest.raises(ValueError) when items == []
