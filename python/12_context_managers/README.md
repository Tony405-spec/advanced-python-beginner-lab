# Module 12 — Context Managers

The `with` statement ensures cleanup happens even if an exception is
raised. Every file open, every database transaction, every lock uses it.

## Concepts covered

- **Why `with`** — guaranteed cleanup, no leaked resources.
- **The protocol** — `__enter__` and `__exit__`.
- **Class-based context managers.**
- **`contextlib.contextmanager`** — generator-based, less boilerplate.
- **`contextlib.suppress`, `redirect_stdout`, `ExitStack`.**
- **Exception handling inside `__exit__`** — returning True suppresses.

## Data Science connection

Database connections, file handles, temporary directories during model
training, changing pandas display options temporarily — all context
managers. Mastering them eliminates entire classes of resource leak
and half-written-file bugs.

## References

- Python docs — Context managers: https://docs.python.org/3/reference/datamodel.html#context-managers
- Python docs — contextlib: https://docs.python.org/3/library/contextlib.html
- Fluent Python, 2nd ed., Chapter 18
