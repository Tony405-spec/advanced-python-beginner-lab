"""Type hints in practice.

Run:
    python python/13_type_hints/examples/01_type_hints.py

To check the types statically:
    pip install mypy
    mypy python/13_type_hints/examples/01_type_hints.py
"""

from typing import Any, Callable, Iterable, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def add(a: int, b: int) -> int:
    return a + b


def avg(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        raise ValueError("avg requires a non-empty iterable")
    return sum(values) / len(values)


def first(items: list[T], default: T | None = None) -> T | None:
    """Return the first item, or default if empty (generic)."""
    return items[0] if items else default


def apply(func: Callable[[T], U], items: list[T]) -> list[U]:
    """Apply func to each item (higher-order with types)."""
    return [func(x) for x in items]


def describe(value: int | str | float) -> str:
    """Union type — accepts any of three types."""
    if isinstance(value, str):
        return f"string of length {len(value)}"
    return f"number of type {type(value).__name__}"


def log(data: Any) -> None:
    """Any — use sparingly."""
    print(f"  log: {data!r}")


def main() -> None:
    print("=== Basic ===")
    print(f"  add(2, 3)         = {add(2, 3)}")

    print("\n=== Iterable ===")
    print(f"  avg([1,2,3,4])    = {avg([1, 2, 3, 4])}")

    print("\n=== Generic ===")
    print(f"  first([10,20,30]) = {first([10, 20, 30])}")
    print(f"  first([], -1)     = {first([], -1)}")

    print("\n=== Higher-order ===")
    print(f"  apply(str, [1,2,3])         = {apply(str, [1, 2, 3])}")
    print(f"  apply(lambda x: x*2, [1,2]) = {apply(lambda x: x * 2, [1, 2])}")

    print("\n=== Union ===")
    print(f"  describe(42)       = {describe(42)}")
    print(f"  describe('hello')  = {describe('hello')}")
    print(f"  describe(3.14)     = {describe(3.14)}")

    print("\n=== Any ===")
    log({"anything": "goes"})


if __name__ == "__main__":
    main()
