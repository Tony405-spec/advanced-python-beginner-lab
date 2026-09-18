"""Tests for Module 02 Exercise 02."""

from python.functions_bootstrap import load_module

ex = load_module(
    "ex02_args_kwargs",
    "python/02_functions/exercises/ex02_args_kwargs.py",
)


def test_total():
    assert ex.total() == 0
    assert ex.total(1, 2, 3) == 6
    assert ex.total(1.5, 2.5) == 4.0


def test_merge_dicts():
    assert ex.merge_dicts() == {}
    assert ex.merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
    assert ex.merge_dicts({"a": 1}, {"a": 3}) == {"a": 3}


def test_describe():
    assert ex.describe(b=2, a=1, c=3) == "a=1, b=2, c=3"
    assert ex.describe() == ""
