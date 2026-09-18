"""Abstract base classes: enforcing contracts.

Run:
    python python/19_abc/examples/01_abcs_in_practice.py
"""

from abc import ABC, abstractmethod
from collections.abc import Iterable, Sequence


class Shape(ABC):
    """Abstract shape — subclasses must implement area and perimeter."""

    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimeter(self) -> float:
        ...

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}, " \
               f"perimeter={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side


class Incomplete(Shape):
    def area(self) -> float:
        return 1.0


def main() -> None:
    print("=== Cannot instantiate abstract class ===")
    try:
        Shape()
    except TypeError as e:
        print(f"  Shape() -> TypeError: {e}")

    print("\n=== Cannot instantiate class missing abstract methods ===")
    try:
        Incomplete()
    except TypeError as e:
        print(f"  Incomplete() -> TypeError: {e}")

    print("\n=== Concrete subclasses work ===")
    for s in [Circle(1), Square(2)]:
        print(f"  {s.describe()}")

    print("\n=== collections.abc: Iterable and Sequence ===")
    def total(xs: Iterable[float]) -> float:
        return sum(xs)

    print(f"  total([1,2,3])     = {total([1, 2, 3])}")
    print(f"  total(range(4))    = {total(range(4))}")
    print(f"  total((1.5, 2.5))  = {total((1.5, 2.5))}")

    print("\n=== isinstance with ABCs ===")
    print(f"  isinstance([1,2], Sequence)  = {isinstance([1, 2], Sequence)}")
    print(f"  isinstance((1,2), Sequence)  = {isinstance((1, 2), Sequence)}")
    print(f"  isinstance(range(3), Sequence) = {isinstance(range(3), Sequence)}")


if __name__ == "__main__":
    main()
