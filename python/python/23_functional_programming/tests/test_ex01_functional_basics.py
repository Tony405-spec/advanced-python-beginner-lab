"""Tests for Module 23 Exercise 01 — functional programming basics.

Run:
    pytest python/23_functional_programming/tests/test_ex01_functional_basics.py -v
"""

import importlib.util
import sys
from pathlib import Path

import pytest


def _load_exercise_module():
    path = (
        Path(__file__).resolve().parents[1]
        / "exercises"
        / "ex01_functional_basics.py"
    )
    spec = importlib.util.spec_from_file_location("ex01_functional_basics", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["ex01_functional_basics"] = module
    spec.loader.exec_module(module)
    return module


ex = _load_exercise_module()


# ---------------------------------------------------------------
# apply_all
# ---------------------------------------------------------------

def test_apply_all_empty():
    assert ex.apply_all([], 5) == 5


def test_apply_all_single():
    assert ex.apply_all([lambda x: x + 1], 3) == 4


def test_apply_all_multiple():
    fns = [lambda x: x + 1, lambda x: x * 2]
    assert ex.apply_all(fns, 3) == 8


def test_apply_all_order_matters():
    # (3 * 2) + 1 == 7, not (3 + 1) * 2 == 8
    fns = [lambda x: x * 2, lambda x: x + 1]
    assert ex.apply_all(fns, 3) == 7


# ---------------------------------------------------------------
# keep_where
# ---------------------------------------------------------------

def test_keep_where_evens():
    assert ex.keep_where(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]


def test_keep_where_all():
    assert ex.keep_where(lambda _: True, [1, 2]) == [1, 2]


def test_keep_where_none():
    assert ex.keep_where(lambda _: False, [1, 2]) == []


# ---------------------------------------------------------------
# transform
# ---------------------------------------------------------------

def test_transform_double():
    assert ex.transform([1, 2, 3], lambda x: x * 2) == [2, 4, 6]


def test_transform_str():
    assert ex.transform([1, 2], str) == ["1", "2"]


def test_transform_empty():
    assert ex.transform([], lambda x: x) == []


# ---------------------------------------------------------------
# fold_sum
# ---------------------------------------------------------------

def test_fold_sum_empty():
    assert ex.fold_sum([]) == 0


def test_fold_sum_ints():
    assert ex.fold_sum([1, 2, 3]) == 6


def test_fold_sum_floats():
    assert ex.fold_sum([1.5, 2.5]) == 4.0
