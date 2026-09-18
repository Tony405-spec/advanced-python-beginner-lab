"""Properties: computed attributes and validation.

Run:
    python python/17_properties/examples/01_properties_in_practice.py
"""


class Circle:
    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"radius must be positive, got {value}")
        self._radius = value

    @property
    def area(self) -> float:
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self) -> float:
        return self._radius * 2

    @diameter.setter
    def diameter(self, value: float) -> None:
        self.radius = value / 2


class Dataset:
    """Lazy-cached mean."""

    def __init__(self, values: list[float]) -> None:
        self._values = list(values)
        self._mean: float | None = None
        self._mean_calls = 0

    @property
    def size(self) -> int:
        return len(self._values)

    @property
    def mean(self) -> float:
        self._mean_calls += 1
        if self._mean is None:
            print(f"  [computing mean over {self.size} values]")
            self._mean = sum(self._values) / self.size if self._values else 0.0
        return self._mean

    @property
    def mean_calls(self) -> int:
        return self._mean_calls


def main() -> None:
    print("=== Properties are attributes, not methods ===")
    c = Circle(5)
    print(f"  c.radius   = {c.radius}")
    print(f"  c.diameter = {c.diameter}")
    print(f"  c.area     = {c.area:.4f}")

    print("\n=== Setter validation ===")
    c.radius = 10
    print(f"  after c.radius = 10: area = {c.area:.4f}")
    try:
        c.radius = -1
    except ValueError as e:
        print(f"  c.radius = -1 -> ValueError: {e}")

    print("\n=== Setter on derived property ===")
    c.diameter = 4
    print(f"  after c.diameter = 4: radius = {c.radius}")

    print("\n=== Lazy caching ===")
    d = Dataset([1, 2, 3, 4, 5])
    print(f"  d.mean      = {d.mean}")
    print(f"  d.mean      = {d.mean}")
    print(f"  d.mean      = {d.mean}")
    print(f"  mean was computed {d.mean_calls} time(s)")


if __name__ == "__main__":
    main()
