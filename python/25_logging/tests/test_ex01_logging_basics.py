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
# ---------------------------------------------------------------
# log_error_with_context
# ---------------------------------------------------------------

def test_log_error_with_context_emits_record(caplog):
    lg = ex.make_logger("test_ctx")
    with caplog.at_level(logging.ERROR, logger="test_ctx"):
        ex.log_error_with_context(lg, "row failed", row=42, column="age")
    assert len(caplog.records) == 1
    rec = caplog.records[0]
    assert rec.levelname == "ERROR"
    assert rec.message == "row failed"
    assert rec.row == 42
    assert rec.column == "age"


# ---------------------------------------------------------------
# count_records_at_level
# ---------------------------------------------------------------

def test_count_records_at_level(caplog):
    lg = ex.make_logger("test_count")

    def emit():
        lg.info("a")
        lg.info("b")
        lg.warning("c")
        lg.error("d")

    with caplog.at_level(logging.DEBUG, logger="test_count"):
        counts = ex.count_records_at_level(caplog, emit)

    assert counts.get("INFO") == 2
    assert counts.get("WARNING") == 1
    assert counts.get("ERROR") == 1


# ---------------------------------------------------------------
# build_file_logger
# ---------------------------------------------------------------

def test_build_file_logger_writes_to_file(tmp_path):
    logfile = tmp_path / "out.log"
    lg = ex.build_file_logger("file_test", str(logfile), level=logging.INFO)
    lg.info("hello file")
    for h in lg.handlers:
        h.flush()
    assert logfile.exists()
    content = logfile.read_text(encoding="utf-8")
    assert "hello file" in content
    assert "INFO" in content


def test_build_file_logger_no_console_handler(tmp_path):
    logfile = tmp_path / "out2.log"
    lg = ex.build_file_logger("file_test2", str(logfile))
    assert len(lg.handlers) == 1
    assert isinstance(lg.handlers[0], logging.FileHandler)


def test_build_file_logger_no_duplicate_handlers(tmp_path):
    logfile = tmp_path / "out3.log"
    ex.build_file_logger("file_test3", str(logfile))
    ex.build_file_logger("file_test3", str(logfile))
    lg = logging.getLogger("file_test3")
    assert len(lg.handlers) == 1


# ---------------------------------------------------------------
# safe_log_context
# ---------------------------------------------------------------

def test_safe_log_context_basic():
    result = ex.safe_log_context(user_id=1, name="ada")
    assert result == {"user_id": 1, "name": "ada"}


def test_safe_log_context_drops_message_key():
    result = ex.safe_log_context(user_id=1, message="ignored")
    assert "message" not in result
    assert result["user_id"] == 1


def test_safe_log_context_drops_underscore_keys():
    result = ex.safe_log_context(user_id=1, _private=True)
    assert "_private" not in result
    assert result["user_id"] == 1


def test_safe_log_context_drops_unserializable():
    result = ex.safe_log_context(user_id=1, obj=object())
    assert "obj" not in result
    assert result["user_id"] == 1
