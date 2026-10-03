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
# ---------------------------------------------------------------
# describe_shape
# ---------------------------------------------------------------

@pytest.mark.parametrize(
    "value,expected",
    [
        (42, "number: 42"),
        (3.14, "number: 3.14"),
        ("hello", "text: hello"),
        ([1, 2, 3], "sequence of 3"),
        ((1, 2), "sequence of 2"),
        ({"a": 1, "b": 2}, "mapping with 2 keys"),
        (None, "unknown"),
        (set(), "unknown"),
    ],
)
def test_describe_shape(value, expected):
    assert ex.describe_shape(value) == expected


# ---------------------------------------------------------------
# transform_command
# ---------------------------------------------------------------

@pytest.mark.parametrize(
    "raw,expected",
    [
        ("quit", "quit"),
        ("EXIT", "quit"),
        ("  Q  ", "quit"),
        ("help", "help"),
        ("?", "help"),
        ("save model_v1", "save: model_v1"),
        ("  Save   model_v1 ", "save: model_v1"),
        ("load checkpoint_a", "load: checkpoint_a"),
        ("", "empty"),
        ("   ", "empty"),
        ("random", "unknown: random"),
    ],
)
def test_transform_command(raw, expected):
    assert ex.transform_command(raw) == expected


# ---------------------------------------------------------------
# route_message
# ---------------------------------------------------------------

@pytest.mark.parametrize(
    "msg,expected",
    [
        ({"type": "user", "id": 42}, "user:42"),
        (
            {"type": "post", "author": "ada", "content": "hi"},
            "post by ada",
        ),
        (
            {"type": "comment", "post_id": 7, "text": "ok"},
            "comment on 7",
        ),
        ({"type": "error", "message": "boom"}, "error: boom"),
        ({"type": "other"}, "unrouted"),
        ({}, "unrouted"),
        ("not a dict", "invalid"),
        (None, "invalid"),
    ],
)
def test_route_message(msg, expected):
    assert ex.route_message(msg) == expected
