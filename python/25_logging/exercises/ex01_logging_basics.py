"""Module 25 Exercise 01 — logging basics (⭐ beginner).

Fill in each function so the tests pass.

Run tests with:
    pytest python/25_logging/tests/test_ex01_logging_basics.py -v
"""

import logging


def make_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Return a logger configured with:
        - the given name
        - the given level
        - a single StreamHandler
        - formatter: "%(levelname)s | %(name)s | %(message)s"

    Calling this function twice with the same name must not add a second
    handler. Return the existing logger if it already has handlers.
    """
    raise NotImplementedError


def log_error_with_context(logger: logging.Logger, message: str, **context) -> None:
    """Log an ERROR with the given message plus structured context.

    Use logger.error(message, extra=context).

    Example:
        log_error_with_context(logger, "row failed", row=42, column="age")
    """
    raise NotImplementedError


def count_records_at_level(caplog, func, *args, **kwargs) -> dict:
    """Run func(*args, **kwargs), then count records by level in caplog.

    Return a dict like {"INFO": 3, "WARNING": 1}.

    caplog is a pytest fixture; the test file will pass it in.
    """
    raise NotImplementedError
def build_file_logger(
    name: str,
    path: str,
    level: int = logging.DEBUG,
) -> logging.Logger:
    """Return a logger that writes to a file at `path`.

    Requirements:
        - Uses logging.FileHandler(path, mode="w", encoding="utf-8")
        - Set the handler formatter to "%(asctime)s | %(levelname)s | %(message)s"
        - Set logger level to `level`
        - Do NOT add a console handler

    Calling twice with the same name should return the existing logger
    (no duplicate handlers).
    """
    raise NotImplementedError


def safe_log_context(**fields) -> dict:
    """Return a dict suitable for logger.info(msg, extra=...).

    Requirements:
        - Drop any key named "message" (reserved by logging)
        - Drop any key starting with underscore
        - Drop any key whose value is not JSON-serializable
          (use json.dumps inside a try/except to test)
        - Return the cleaned dict

    Example:
        safe_log_context(user_id=1, password="x", _internal=True) ->
        {"user_id": 1, "password": "x"}
    """
    raise NotImplementedError
