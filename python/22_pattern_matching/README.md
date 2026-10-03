# Module 22 — Pattern Matching

`match` / `case` (introduced in Python 3.10) is structural pattern matching —
a different tool from `if`/`elif`. It matches against the *shape* of data,
not just equality.

## Concepts covered

- **Literal patterns** — `case 200:`
- **Capture patterns** — `case x:`
- **Wildcard** — `case _:`
- **OR patterns** — `case "yes" | "y" | "true":`
- **Sequence patterns** — `case [first, *rest]:`
- **Mapping patterns** — `case {"type": "user", "id": uid}:`
- **Class patterns** — `case Point(x=0, y=0):`
- **Guards** — `case x if x > 0:`

## Data Science connection

Parsing API responses, dispatching on record type in ETL pipelines,
handling heterogeneous JSON payloads, and command routing in CLI tools.

## Files

- `examples/01_basics.py`
- `examples/02_structural_matching.py`
- `exercises/`
- `tests/`

## References

- PEP 634: https://peps.python.org/pep-0634/
- Python docs: https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
