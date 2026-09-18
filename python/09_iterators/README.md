# Module 09 — Iterators

The iterator protocol: `__iter__` and `__next__`. How `for` loops actually work.
Why you can iterate a list twice but a file only once.

## Concepts covered

- **Iterable vs iterator** — an iterable has `__iter__`; an iterator has `__next__`.
- **The `for` loop desugared** — `iter()` + `StopIteration`.
- **Custom iterators** — writing a class with `__iter__` and `__next__`.
- **`iter()` with two arguments** — the sentinel form.
- **Why files exhaust** — iterators are single-use.
- **`itertools` introduction** — `count`, `cycle`, `chain`, `islice`, `takewhile`.

## Data Science connection

Streaming CSV rows, batching API responses, and iterating over a
`DataLoader` all rely on the iterator protocol. Understanding it lets you
process data larger than memory and reason about why some objects
"run out" after one pass.

## References

- Python docs — Iterators: https://docs.python.org/3/tutorial/classes.html#iterators
- Python docs — itertools: https://docs.python.org/3/library/itertools.html
- Fluent Python, 2nd ed., Chapter 17
