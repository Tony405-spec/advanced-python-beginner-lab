# Module 20 — Protocols

A Protocol is structural typing: "any object with these methods
qualifies." No inheritance needed. This is the modern, Pythonic
alternative to ABCs for most interface definitions.

## Concepts covered

- **`typing.Protocol`** — structural subtyping.
- **Runtime checkable protocols** — `@runtime_checkable`.
- **Protocols vs. ABCs** — when to use which.
- **Duck typing formalized** — a Protocol makes the informal contract checkable.
- **Generic protocols** — `Protocol[T]`.

## Data Science connection

When you pass a DataFrame-like object to a function, or a model-like
object to a training loop, you're relying on duck typing. Protocols
let you state those contracts explicitly and have mypy enforce them.

## References

- Python docs — typing.Protocol: https://docs.python.org/3/library/typing.html#typing.Protocol
- PEP 544: https://peps.python.org/pep-0544/
- Fluent Python, 2nd ed., Chapter 13
