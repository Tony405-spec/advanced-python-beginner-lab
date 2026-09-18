# Module 13 — Type Hints

Type hints are documentation that tools can check. They do not affect
runtime. They improve readability, catch bugs early with mypy, and unlock
better IDE support.

## Concepts covered

- **Basic annotations** — `int`, `str`, `float`, `bool`, `None`.
- **Containers** — `list[int]`, `dict[str, float]`, `set[str]`, `tuple[int, ...]`.
- **`Optional`** — `X | None` (3.10+) or `Optional[X]`.
- **Union** — `int | str` or `Union[int, str]`.
- **Callables** — `Callable[[int, int], int]`.
- **`Any`** — the escape hatch; use sparingly.
- **`TypeVar`** and **`Generic`** — reusable typed containers.
- **`Protocol`** — structural typing (deep dive in Module 20).
- **mypy** — actually checking the hints.

## Data Science connection

Typed function signatures make pipelines self-documenting. Typed
dataclasses (Module 14) make model configs explicit. mypy catches the
"passed a DataFrame where a Series was expected" bug before it runs.

## References

- Python docs — typing: https://docs.python.org/3/library/typing.html
- mypy docs: https://mypy.readthedocs.io/
- Fluent Python, 2nd ed., Chapter 8
