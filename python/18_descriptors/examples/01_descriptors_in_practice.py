"""Descriptors: the machinery behind property, classmethod, and more.

Run:
    python python/18_descriptors/examples/01_descriptors_in_practice.py
"""


class Positive:
    """Data descriptor that enforces positivity on assignment."""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive, got {value}")
        obj.__dict__[self.name] = value


class MyProperty:
    """Minimal reimplementation of @property as a data descriptor."""

    def __init__(self, fget):
        self.fget = fget
        self.name = fget.__name__

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.fget(obj)


class Temperature:
    celsius = Positive()

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @MyProperty
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32


def main() -> None:
    print("=== Positive descriptor ===")
    t = Temperature(25)
    print(f"  t.celsius = {t.celsius}")
    t.celsius = 30
    print(f"  after t.celsius = 30: {t.celsius}")
    try:
        t.celsius = -5
    except ValueError as e:
        print(f"  t.celsius = -5 -> ValueError: {e}")

    print("\n=== MyProperty descriptor ===")
    print(f"  t.fahrenheit = {t.fahrenheit:.1f}")

    print("\n=== Descriptor accessed on the class returns itself ===")
    print(f"  Temperature.celsius       = {Temperature.celsius}")
    print(f"  Temperature.fahrenheit    = {Temperature.fahrenheit}")


if __name__ == "__main__":
    main()
