# Module 23 — Functional Programming

Python is not a functional language, but it borrows heavily from that
tradition. This module covers the functional tools Python *does* provide,
when they clarify code, and when they don't.

## Concepts covered

- **Pure functions** — same input, same output, no side effects.
- **Immutability** — preferring `tuple` over `list`, returning new
  objects rather than mutating.
- **`map`, `filter`, `reduce`** — the classic trio.
- **`functools`** — `partial`, `reduce`, `lru_cache`, `singledispatch`.
- **`itertools`** — `chain`, `groupby`, `product`, `combinations`.
- **Composition** — building bigger functions from smaller ones.
- **When NOT to be functional** — readability always wins.

## Data Science connection

Feature pipelines are chains of pure transformations. `functools.partial`
freezes hyperparameters. `itertools.product` generates hyperparameter
grids. `lru_cache` memoizes expensive feature computations.

## References

- Python docs — functools: https://docs.python.org/3/library/functools.html
- Python docs — itertools: https://docs.python.org/3/library/itertools.html
- Fluent Python, 2nd ed., Chapters 7 & 17
