"""Tests for Module 22 Exercise 01 — pattern matching basics.

Run:
    pytest python/22_pattern_matching/tests/test_ex01_pattern_basics.py -v
"""

import importlib.util
import sys
from pathlib import Path

import pytest


def _load_exercise_module():
    """Load the exercise file by path (not a package)."""
    path = (
        Path(__file__).resolve().parents[1]
        / "exercises"
        / "ex01_pattern_basics.py"
    )
    spec = importlib.util.spec_from_file_location("ex01_pattern_basics", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["ex01_pattern_basics"] = module
    spec.loader.exec_module(module)
    return module


ex = _load_exercise_module()


# ---------------------------------------------------------------
# http_class
# ---------------------------------------------------------------

@pytest.mark.parametrize(
    "code,expected",
    [
        (100, "informational"),
        (199, "informational"),
        (200, "success"),
        (204, "success"),
        (299, "success"),
        (301, "redirect"),
        (399, "redirect"),
        (400, "client error"),
        (404, "client error"),
        (499, "client error"),
        (500, "server error"),
        (503, "server error"),
        (599, "server error"),
        (99, "invalid"),
        (600, "invalid"),
        (0, "invalid"),
        (-1, "invalid"),
    ],
)
def test_http_class(code, expected):
    assert ex.http_class(code) == expected


# ---------------------------------------------------------------
# parse_date_like
# ---------------------------------------------------------------

@pytest.mark.parametrize(
    "value,expected",
    [
        ((2024, 1, 15), (2024, 1, 15)),
        ([2024, 1, 15], (2024, 1, 15)),
        ({"y": 2024, "m": 1, "d": 15}, (2024, 1, 15)),
        ("2024-01-15", None),
        ({"year": 2024}, None),
        (None, None),
        (42, None),
    ],
)
def test_parse_date_like(value, expected):
    assert ex.parse_date_like(value) == expected
