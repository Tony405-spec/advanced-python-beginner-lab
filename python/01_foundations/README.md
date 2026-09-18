# Module 01 — Python Foundations

Before decorators, generators, async, or descriptors, there is the substrate
every one of those features rests on: **names, objects, mutability, truthiness,
and scope**. Every "weird Python bug" in professional code traces back to one
of these five topics.

This module locks those five down.

## Why this matters for Data Science

Most pandas, numpy, or ML bugs you will see in practice are one of:

- **Aliasing.** Two variables point at the same mutable object, one gets
  mutated, the other appears to change "mysteriously".
- **Truthiness.** `if df:` is not the same as `if df is not None:`. Empty
  DataFrames, zero-length arrays, and NaN all have surprising truthiness.
- **Scope.** Closures over loop variables, `global` misuse, and late-binding
  bugs in list comprehensions.
- **Mutability in default arguments.** `def f(x, acc=[]):` accumulates across
  calls — this bites every Python programmer once.

Getting these right at the foundations level is cheaper than debugging them at
2 AM in a production ML pipeline.

## Concepts covered

### 1. Names vs. objects

In Python, a variable is a **name bound to an object**, not a box holding a
value. `a = 5` binds the name `a` to the integer object `5`. `b = a` binds a
*second* name to the *same* object.

    a = 5
    b = a
    a = 6      # a now points to a *different* object
    print(b)   # 5  — b still points at the original 5

This matters because the rule differs for mutable objects:

    a = [1, 2, 3]
    b = a
    a.append(4)
    print(b)   # [1, 2, 3, 4]  — b sees the change, same list

### 2. Identity vs. equality

- `is` compares **identity** (same object in memory).
- `==` compares **equality** (same value, using `__eq__`).

Rule of thumb:

- Use `is` only for `None`, `True`, `False`, and sentinel objects.
- Use `==` for values.

    a = [1, 2, 3]
    b = [1, 2, 3]
    a == b    # True   — same values
    a is b    # False  — different objects

### 3. Mutability

| Immutable        | Mutable          |
|------------------|------------------|
| `int`, `float`   | `list`           |
| `str`            | `dict`           |
| `tuple`          | `set`            |
| `frozenset`      | `bytearray`      |
| `bytes`          | user classes by default |

Immutable objects can be safely shared; mutable ones cannot. Any function that
receives a mutable argument can mutate it — unless you copy first.

### 4. Truthiness

Every object has a truth value. The rules:

- `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()` → falsy
- Everything else → truthy
- A custom class controls this via `__bool__` then `__len__`.

The Data Science trap:

    import pandas as pd
    df = pd.DataFrame()
    bool(df)      # raises ValueError
    if df: ...    # raises ValueError — not False!

Always use explicit checks in data code:

    if df is not None and not df.empty: ...

### 5. Scope rules (LEGB)

Python resolves names in this order:

1. **L**ocal — inside the current function.
2. **E**nclosing — any enclosing function (closures).
3. **G**lobal — module level.
4. **B**uilt-in — `len`, `print`, `ValueError`, etc.

Assignment creates a **local** name unless declared otherwise:

    x = 10
    def f():
        x = 20       # creates a new LOCAL x, does not touch the global one

To modify the global from inside:

    def g():
        global x
        x = 20       # now modifies the global x

You should almost never do this. Closures or return values are cleaner.

### 6. Default argument trap

    def add(item, bucket=[]):
        bucket.append(item)
        return bucket

    add(1)    # [1]
    add(2)    # [1, 2]  ← surprise!

The default `[]` is evaluated **once**, at function definition time, and
mutated in place across all calls. Correct pattern:

    def add(item, bucket=None):
        if bucket is None:
            bucket = []
        bucket.append(item)
        return bucket

## Files in this module

- `examples/01_immutable_vs_mutable.py` — runnable demonstration of the five
  concepts above.
- `exercises/` — challenges for you to solve.
- `tests/` — pytest suite that verifies the exercise solutions.

## Run the example

    python python/01_foundations/examples/01_immutable_vs_mutable.py

## References

- Python docs — Data model: https://docs.python.org/3/reference/datamodel.html
- Python docs — Execution model (scope): https://docs.python.org/3/reference/executionmodel.html
- Fluent Python, 2nd ed., Chapters 6 & 7 — Luciano Ramalho
- Effective Python, 3rd ed., Items 1–4 — Brett Slatkin
