"""Enums: named constants, validation, and comparison safety.

Run:
    python python/15_enums/examples/01_enums_in_practice.py
"""

from enum import Enum, IntEnum, auto, unique


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Status(IntEnum):
    PENDING = 0
    RUNNING = 1
    DONE = 2
    FAILED = 3


@unique
class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


def describe_color(color: Color) -> str:
    if color is Color.RED:
        return "warm"
    if color is Color.GREEN:
        return "cool"
    return "cold"


def main() -> None:
    print("=== Basic Enum ===")
    print(f"  Color.RED          = {Color.RED}")
    print(f"  Color.RED.name     = {Color.RED.name}")
    print(f"  Color.RED.value    = {Color.RED.value}")
    print(f"  Color('GREEN'?)    -> {Color['GREEN']!r}")

    print("\n=== Identity comparison ===")
    print(f"  Color.RED is Color.RED   = {Color.RED is Color.RED}")
    print(f"  Color.RED == Color.RED   = {Color.RED == Color.RED}")

    print("\n=== IntEnum ===")
    s = Status.RUNNING
    print(f"  Status.RUNNING         = {s}")
    print(f"  int(Status.RUNNING)    = {int(s)}")
    print(f"  Status.RUNNING == 1    = {s == 1}")

    print("\n=== @unique prevents duplicate values ===")
    print(f"  Direction.NORTH.value  = {Direction.NORTH.value}")

    print("\n=== Iterating ===")
    for c in Color:
        print(f"  {c.name:>6} = {c.value}  ({describe_color(c)})")

    print("\n=== Lookup by value ===")
    print(f"  Color(2)            = {Color(2)}")
    print(f"  Status(3)           = {Status(3)}")

    print("\n=== Pattern matching (Python 3.10+) ===")
    def classify(c: Color) -> str:
        match c:
            case Color.RED:
                return "stop"
            case Color.GREEN:
                return "go"
            case _:
                return "wait"

    for c in Color:
        print(f"  {c.name:>6} -> {classify(c)}")


if __name__ == "__main__":
    main()
