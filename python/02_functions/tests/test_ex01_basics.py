"""Tests for Module 02 Exercise 01."""

import pytest

from python.functions_bootstrap import load_module

ex = load_module(
    "ex01_basics",
    "python/02_functions/exercises/ex01_basics.py",
)


def test_add():
    assert ex.add(2, 3) == 5
    assert ex.add(-1, 1) == 0
    assert ex.add(0, 0) == 0


def test_apply():
    assert ex.apply(lambda x: x * 2, 5) == 10
    assert ex.apply(str, 42) == "42"


def test_apply_n():
    assert ex.apply_n(lambda x: x + 1, 0, 3) == 3
    assert ex.apply_n(lambda x: x * 2, 1, 4) == 16
    assert ex.apply_n(lambda x: x, 7, 0) == 7


def test_make_greeting():
    hello = ex.make_greeting("Hello")
    assert hello("Ada") == "Hello, Ada"
    assert hello("Grace") == "Hello, Grace"
