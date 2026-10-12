"""Tests for Module 25 Exercise 01 — logging basics.

Run:
    pytest python/25_logging/tests/test_ex01_logging_basics.py -v
"""

import importlib.util
import logging
import sys
from pathlib import Path

import pytest


def _load_exercise_module():
    path = (
        Path(__file__).resolve().parents[1]
        / "exercises"
        / "ex01_logging_basics.py"
    )
    spec = importlib.util.spec_from_file_location("ex01_logging_basics", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["ex01_logging_basics"] = module
    spec.loader.exec_module(module)
    return module


ex = _load_exercise_module()


@pytest.fixture(autouse=True)
def clear_loggers():
    """Remove handlers from any logger created during tests."""
    yield
    for name in list(logging.Logger.manager.loggerDict):
        lg = logging.getLogger(name)
        if lg.handlers:
            lg.handlers.clear()


# ---------------------------------------------------------------
# make_logger
# ---------------------------------------------------------------

def test_make_logger_returns_logger():
    lg = ex.make_logger("test_a")
    assert isinstance(lg, logging.Logger)
    assert lg.name == "test_a"
    assert lg.level == logging.INFO


def test_make_logger_custom_level():
    lg = ex.make_logger("test_b", level=logging.DEBUG)
    assert lg.level == logging.DEBUG


def test_make_logger_has_one_handler():
    lg = ex.make_logger("test_c")
    assert len(lg.handlers) == 1
    assert isinstance(lg.handlers[0], logging.StreamHandler)


def test_make_logger_no_duplicate_handlers():
    ex.make_logger("test_d")
    ex.make_logger("test_d")
    lg = logging.getLogger("test_d")
    assert len(lg.handlers) == 1


def test_make_logger_formatter():
    lg = ex.make_logger("test_e")
    fmt = lg.handlers[0].formatter._fmt
    assert "%(levelname)s" in fmt
    assert "%(name)s" in fmt
    assert "%(message)s" in fmt
