"""Module 22 Exercise 01 — pattern matching basics ( beginner).

Fill in each function so that the corresponding tests pass.

Run tests with:
    pytest python/22_pattern_matching/tests/test_ex01_pattern_basics.py -v
"""

from typing import Any


def http_class(code: int) -> str:
    """Return the HTTP class name for a status code.

    Rules:
        100–199 -> "informational"
        200–299 -> "success"
        300–399 -> "redirect"
        400–499 -> "client error"
        500–599 -> "server error"
        anything else -> "invalid"

    Use match/case with guards.
    """
    raise NotImplementedError


def parse_date_like(value: Any) -> tuple[int, int, int] | None:
    """Parse common date shapes into (year, month, day).

    Accepted shapes:
        (2024, 1, 15)         -> (2024, 1, 15)
        [2024, 1, 15]         -> (2024, 1, 15)
        {"y": 2024, "m": 1, "d": 15} -> (2024, 1, 15)

    Anything else -> None

    Use match/case with sequence, mapping, and class patterns.
    """
    raise NotImplementedError


def describe_shape(shape: Any) -> str:
    """Describe a shape-like object.

    Accepts:
        int or float  -> "number: <value>"
        str           -> "text: <value>"
        list or tuple -> "sequence of <n>"
        dict          -> "mapping with <n> keys"
        anything else -> "unknown"
    """
    raise NotImplementedError
def transform_command(command: str) -> str:
    """Return a canonical form for a user command.

    Rules (case-insensitive, ignore surrounding whitespace):
        quit | exit | q     -> "quit"
        help | h | ?        -> "help"
        save <name>         -> "save: <name>"
        load <name>         -> "load: <name>"
        empty string        -> "empty"
        anything else       -> "unknown: <original>"

    The "save" and "load" commands take one argument (the name).
    Example: "  Save   model_v1 " -> "save: model_v1"

    Use match/case with capture and OR patterns.
    """
    raise NotImplementedError


def route_message(msg: dict) -> str:
    """Route a message dict to its handler description.

    Rules:
        {"type": "user", "id": int} -> "user:<id>"
        {"type": "post", "author": str, "content": str} -> "post by <author>"
        {"type": "comment", "post_id": int, "text": str} -> "comment on <post_id>"
        {"type": "error", "message": str} -> "error: <message>"
        any other dict -> "unrouted"
        not a dict -> "invalid"

    Use match/case with mapping patterns and class patterns.
    """
    raise NotImplementedError
