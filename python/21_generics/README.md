# Module 21 — Generics

Generics let you write one implementation that works for many types
while preserving type information. `list[int]` is more informative than
`list`. `Stack[T]` works for any T.

## Concepts covered

- **`TypeVar`** — a placeholder for "some type".
- **Generic functions** — `def first(xs: list[T]) -> T`.
- **Generic classes** — `class Stack(Generic[T])`.
- **Constraints** — `TypeVar("T", int, float)`.
- **Bound** — `TypeVar("T", bound=Comparable)`.
- **`Protocol[T]`** — generic protocols (from Module 20).
- **PEP 695 (3.12+)** — the new `type` and `class C[T]:` syntax.

## Data Science connection

A generic `Batch[T]` for training, a generic `Pipeline[In, Out]` for
transformations, a generic cache for feature vectors — generics keep
type information intact through composition.

## References

- Python docs — typing Generics: https://docs.python.org/3/library/typing.html#user-defined-generic-types
- PEP 484: https://peps.python.org/pep-0484/
- PEP 695: https://peps.python.org/pep-0695/
