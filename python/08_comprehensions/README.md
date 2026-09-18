# Module 08 — Comprehensions

List, dict, set, and generator comprehensions. When to use them, when not to,
and how to avoid turning readable code into a puzzle.

## Concepts covered

- **List comprehensions** — `[f(x) for x in xs if cond(x)]`
- **Dict comprehensions** — `{k: v for k, v in pairs}`
- **Set comprehensions** — `{f(x) for x in xs}`
- **Generator expressions** — `(f(x) for x in xs)` — lazy, memory-efficient
- **Nested comprehensions** — flattening, matrix operations
- **Conditional expressions** — `a if cond else b`
- **When NOT to use** — side effects, deep nesting, unclear logic

## Data Science connection

Feature engineering is largely list/dict comprehensions over rows.
Parsing API responses, transforming DataFrame columns, and building
feature dicts are all comprehension territory. Generator expressions
matter when you stream large data instead of loading it into memory.

## References

- Python docs — Comprehensions: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- Effective Python, 3rd ed., Items 27–28
