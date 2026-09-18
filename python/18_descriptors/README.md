# Module 18 — Descriptors

Descriptors are the machinery behind `@property`, `@classmethod`,
`@staticmethod`, and SQLAlchemy's columns. If you can write one, you
understand why half of Python's "magic" works.

## Concepts covered

- **The descriptor protocol** — `__get__`, `__set__`, `__delete__`.
- **Data vs. non-data descriptors** — why the difference matters.
- **Attribute lookup order** — the full algorithm.
- **Reimplementing `@property`** as a descriptor.
- **Reimplementing `@classmethod`** as a descriptor.
- **Validated attributes** — descriptors as reusable validators.
- **`__set_name__`** — for auto-naming.

## Data Science connection

Framework code (SQLAlchemy, Pydantic, Django, attrs) uses descriptors
for declarative field definitions. Understanding descriptors makes
those frameworks feel less like magic and more like predictable design.

## References

- Python docs — Descriptor protocol: https://docs.python.org/3/howto/descriptor.html
- Fluent Python, 2nd ed., Chapter 23
