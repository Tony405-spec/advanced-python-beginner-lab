"""Dunder methods: making classes feel native to Python.

Run:
    python python/16_dunder_methods/examples/01_dunder_methods.py
"""

from typing import Iterator


class Vector:
    """A 2D vector with full operator support."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0


class Playlist:
    """A container-like class with len, indexing, and iteration."""

    def __init__(self, songs: list[str]) -> None:
        self._songs = list(songs)

    def __len__(self) -> int:
        return len(self._songs)

    def __getitem__(self, index: int) -> str:
        return self._songs[index]

    def __contains__(self, song: str) -> bool:
        return song in self._songs

    def __iter__(self) -> Iterator[str]:
        return iter(self._songs)


class Multiplier:
    """A callable object — instances behave like functions."""

    def __init__(self, factor: float) -> None:
        self.factor = factor

    def __call__(self, value: float) -> float:
        return value * self.factor


def main() -> None:
    print("=== __repr__ vs __str__ ===")
    v = Vector(3, 4)
    print(f"  repr(v) = {v!r}")
    print(f"  str(v)  = {v}")

    print("\n=== __add__, __sub__, __mul__, __abs__ ===")
    a = Vector(1, 2)
    b = Vector(3, 4)
    print(f"  a + b   = {a + b}")
    print(f"  b - a   = {b - a}")
    print(f"  a * 10  = {a * 10}")
    print(f"  10 * a  = {10 * a}")
    print(f"  abs(b)  = {abs(b)}")

    print("\n=== __eq__ and __hash__ ===")
    print(f"  Vector(1,2) == Vector(1,2) = {Vector(1, 2) == Vector(1, 2)}")
    print(f"  len({{Vector(0,0), Vector(1,1), Vector(0,0)}}) = "
          f"{len({Vector(0, 0), Vector(1, 1), Vector(0, 0)})}")

    print("\n=== Container dunders ===")
    pl = Playlist(["a", "b", "c"])
    print(f"  len(pl)          = {len(pl)}")
    print(f"  pl[0]            = {pl[0]!r}")
    print(f"  pl[-1]           = {pl[-1]!r}")
    print(f"  'b' in pl        = {'b' in pl}")
    print(f"  list(pl)         = {list(pl)}")

    print("\n=== Callable object ===")
    double = Multiplier(2)
    print(f"  double(21)       = {double(21)}")
    print(f"  callable(double) = {callable(double)}")


if __name__ == "__main__":
    main()
