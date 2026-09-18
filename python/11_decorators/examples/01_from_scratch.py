"""Decorators from first principles.

Run:
    python python/11_decorators/examples/01_from_scratch.py
"""

import functools
import time


# ---------------------------------------------------------------
# 1. A function that takes a function and returns a function.
# ---------------------------------------------------------------

def shout(func):
    """Return a new function that calls func and uppercases the result."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def greet(name: str) -> str:
    return f"hello, {name}"


loud_greet = shout(greet)
print("=== Manual application ===")
print(f"  greet('ada')      = {greet('ada')!r}")
print(f"  loud_greet('ada') = {loud_greet('ada')!r}")


# ---------------------------------------------------------------
# 2. The @ syntax — same thing, cleaner.
# ---------------------------------------------------------------

@shout
def greet_decorated(name: str) -> str:
    return f"hello, {name}"


print("\n=== @ syntax ===")
print(f"  greet_decorated('ada') = {greet_decorated('ada')!r}")


# ---------------------------------------------------------------
# 3. Why functools.wraps matters.
# ---------------------------------------------------------------

def timed_naive(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"  [naive] {time.perf_counter() - start:.6f}s")
        return result
    return wrapper


def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"  [wraps] {time.perf_counter() - start:.6f}s")
        return result
    return wrapper


@timed_naive
def add_naive(a: int, b: int) -> int:
    return a + b


@timed
def add_wrapped(a: int, b: int) -> int:
    return a + b


print("\n=== functools.wraps preserves metadata ===")
print(f"  add_naive.__name__ = {add_naive.__name__!r}  (lost)")
print(f"  add_wrapped.__name__ = {add_wrapped.__name__!r}  (preserved)")

add_naive(2, 3)
add_wrapped(2, 3)
