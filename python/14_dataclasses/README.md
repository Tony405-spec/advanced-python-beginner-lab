# Module 14 — Dataclasses

`@dataclass` removes the boilerplate from classes whose main job is to
hold data. One decorator replaces `__init__`, `__repr__`, `__eq__`, and
more.

## Concepts covered

- **Basic `@dataclass`** — automatic `__init__`, `__repr__`, `__eq__`.
- **Defaults** — and why mutable defaults still need `field(default_factory=...)`.
- **`field()`** — control over individual fields.
- **`frozen=True`** — immutable dataclasses (hashable, safe as dict keys).
- **`order=True`** — automatic comparison methods.
- **Inheritance** — how dataclasses inherit.
- **`__post_init__`** — run code after the auto-generated `__init__`.
- **`asdict()` and `astuple()`** — conversion helpers.

## Data Science connection

Config objects for training runs, feature definitions, API response
models, experiment metadata — all naturally dataclasses. They document
the shape of your data and give you free equality, repr, and typing.

## References

- Python docs — dataclasses: https://docs.python.org/3/library/dataclasses.html
- Fluent Python, 2nd ed., Chapter 5
