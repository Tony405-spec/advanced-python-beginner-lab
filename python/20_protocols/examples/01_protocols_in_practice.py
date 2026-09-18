"""Protocols: structural typing without inheritance.

Run:
    python python/20_protocols/examples/01_protocols_in_practice.py
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Sized(Protocol):
    def __len__(self) -> int:
        ...


@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str:
        ...


class Circle:
    def draw(self) -> str:
        return "○"


class Square:
    def draw(self) -> str:
        return "□"


class NotDrawable:
    def paint(self) -> str:
        return "no"


def render(item: Drawable) -> str:
    """Any object with a .draw() method works here — no inheritance required."""
    return item.draw()


def measure(x: Sized) -> int:
    return len(x)


def main() -> None:
    print("=== Structural typing: no inheritance required ===")
    print(f"  render(Circle())    = {render(Circle())}")
    print(f"  render(Square())    = {render(Square())}")

    print("\n=== runtime_checkable isinstance works ===")
    print(f"  isinstance(Circle(), Drawable)     = {isinstance(Circle(), Drawable)}")
    print(f"  isinstance(NotDrawable(), Drawable) = {isinstance(NotDrawable(), Drawable)}")

    print("\n=== Sized protocol matches many things ===")
    print(f"  measure([1,2,3])     = {measure([1, 2, 3])}")
    print(f"  measure('hello')     = {measure('hello')}")
    print(f"  measure({{'a': 1}})    = {measure({'a': 1})}")
    print(f"  measure(range(10))   = {measure(range(10))}")

    print("\n=== Sized is a runtime_checkable protocol ===")
    print(f"  isinstance([1,2], Sized) = {isinstance([1, 2], Sized)}")
    print(f"  isinstance(5, Sized)     = {isinstance(5, Sized)}")


if __name__ == "__main__":
    main()
