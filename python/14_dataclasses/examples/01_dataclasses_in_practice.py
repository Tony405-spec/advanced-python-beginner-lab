"""Dataclasses: from boilerplate class to @dataclass to frozen config.

Run:
    python python/14_dataclasses/examples/01_dataclasses_in_practice.py
"""

from dataclasses import asdict, dataclass, field
from typing import Any


# --- 1. The old way: manual boilerplate ---

class ManualPoint:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"ManualPoint(x={self.x!r}, y={self.y!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ManualPoint):
            return NotImplemented
        return self.x == other.x and self.y == other.y


# --- 2. The dataclass way: one decorator ---

@dataclass
class Point:
    x: float
    y: float


# --- 3. Defaults and field() ---

@dataclass
class TrainingConfig:
    model_name: str
    learning_rate: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)


# --- 4. Frozen and hashable ---

@dataclass(frozen=True)
class Feature:
    name: str
    dtype: str
    nullable: bool = False


# --- 5. __post_init__ ---

@dataclass
class Range:
    low: float
    high: float

    def __post_init__(self) -> None:
        if self.low >= self.high:
            raise ValueError(f"low must be < high, got {self.low} >= {self.high}")


def main() -> None:
    print("=== Manual class boilerplate ===")
    mp1 = ManualPoint(1, 2)
    mp2 = ManualPoint(1, 2)
    print(f"  repr: {mp1}")
    print(f"  equality: {mp1 == mp2}")

    print("\n=== Dataclass: same result, less code ===")
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(f"  repr: {p1}")
    print(f"  equality: {p1 == p2}")

    print("\n=== Defaults and field(default_factory=...) ===")
    cfg = TrainingConfig(model_name="resnet18")
    cfg.tags.append("baseline")
    cfg.metrics["accuracy"] = 0.91
    other = TrainingConfig(model_name="resnet18")
    print(f"  cfg       = {cfg}")
    print(f"  other     = {other}")
    print(f"  tags of other (independent) = {other.tags}")

    print("\n=== Frozen dataclass ===")
    f = Feature("age", "int")
    print(f"  feature = {f}")
    try:
        f.name = "other"
    except Exception as e:
        print(f"  cannot mutate frozen: {type(e).__name__}: {e}")

    print("\n=== __post_init__ validation ===")
    r = Range(0.0, 1.0)
    print(f"  valid range: {r}")
    try:
        Range(1.0, 0.0)
    except ValueError as e:
        print(f"  invalid range -> {e}")

    print("\n=== asdict() ===")
    print(f"  asdict(cfg) = {asdict(cfg)}")


if __name__ == "__main__":
    main()
