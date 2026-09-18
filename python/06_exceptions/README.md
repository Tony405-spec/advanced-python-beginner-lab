# Module 06 — Exceptions

Errors are inevitable. Handling them well is what separates robust code
from fragile code.

## Concepts covered

- **Exception hierarchy** — `BaseException` → `Exception` → specific types.
- **`try` / `except` / `else` / `finally`** — each clause's purpose.
- **Raising** — `raise`, `raise X from Y` for chaining.
- **Custom exceptions** — when and how to define them.
- **`EAFP` vs `LBYL`** — Python's preference for "easier to ask forgiveness".
- **Context managers introduction** — `with` blocks (deep dive in Module 12).
- **Common anti-patterns** — bare `except`, silent swallowing, `except Exception: pass`.

## Data Science connection

Data pipelines fail in interesting ways: missing files, malformed rows,
network errors on API calls, division by zero during feature engineering.
Robust pipelines catch specific exceptions and log them, rather than
crashing on the first bad row or silently dropping records.

## References

- Python docs — Errors and exceptions: https://docs.python.org/3/tutorial/errors.html
- Effective Python, 3rd ed., Items 76–81
