# Module 11 — Decorators

A decorator is a function that takes a function and returns a function.
That is the entire concept. Everything else is syntax sugar and variations.

## Concepts covered

- **Functions as arguments and return values** (recap from Module 02).
- **Basic decorator** — the `@decorator` syntax desugared.
- **`functools.wraps`** — preserving metadata.
- **Decorators with arguments** — the "decorator factory" pattern.
- **Stacking decorators** — order matters.
- **Class-based decorators** — `__call__`.
- **Real uses** — logging, timing, retry, caching, access control.

## Data Science connection

Timing feature extraction, caching expensive model calls, retrying flaky
API requests, logging every training run — decorators keep that
cross-cutting logic out of your core code.

## References

- Python docs — Decorators: https://docs.python.org/3/glossary.html#term-decorator
- Fluent Python, 2nd ed., Chapter 9
- Effective Python, 3rd ed., Items 33–35
