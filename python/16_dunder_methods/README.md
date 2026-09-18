# Module 16 — Dunder Methods

Dunder ("double underscore") methods let your classes integrate with
Python's syntax: `len(x)`, `x + y`, `for i in x`, `x[key]`, `with x`,
`print(x)`, and so on. They are how Python achieves operator overloading.

## Concepts covered

- **`__repr__` vs `__str__`** — debugging vs. user-facing.
- **`__eq__`, `__hash__`, `__lt__`, etc.** — comparisons and ordering.
- **`__add__`, `__mul__`, `__sub__`, ...** — arithmetic operators.
- **`__len__`, `__getitem__`, `__setitem__`, `__contains__`** — container protocol.
- **`__iter__`, `__next__`** — iteration protocol (see Module 09).
- **`__enter__`, `__exit__`** — context managers (see Module 12).
- **`__call__`** — callable objects.

## Data Science connection

Custom metrics that support `+` and `-`, models that support `len()`,
feature vectors with `[]` access, experiment objects that print nicely
in a notebook — all dunder methods. They make your abstractions feel
native to Python.

## References

- Python docs — Data model: https://docs.python.org/3/reference/datamodel.html
- Fluent Python, 2nd ed., Chapters 1, 11–13
