# Module 02 — Functions

Functions are Python's primary unit of abstraction. This module goes beyond
"how to define a function" into the mechanics that make decorators, closures,
functools, and functional programming possible.

## Why this matters

Every advanced Python tool — decorators, generators, context managers, async —
rests on the fact that **functions are ordinary objects** in Python. They can
be stored in variables, passed as arguments, returned from other functions,
and given attributes. Once you internalize that, an enormous amount of Python
stops feeling like magic.

## Concepts covered

- **Functions are objects** — a `def` statement binds a function object to a name.
- **Full argument semantics** — positional-only `/`, keyword-only `*`, `*args`, `**kwargs`.
- **Higher-order functions** — functions that take or return functions.
- **Lambdas** — anonymous single-expression functions.
- **`functools` introduction** — `partial`, `reduce`, and a first look at caching.

## Data Science connection

`pandas.apply`, `sklearn` transformers, custom loss functions, and feature
pipelines all pass functions around. Understanding functions-as-objects is
what makes those APIs feel natural rather than mysterious.

## Files

- `examples/01_functions_are_objects.py`
- `examples/02_argument_semantics.py`
- `examples/03_higher_order_and_lambdas.py`
- `exercises/` — challenges
- `tests/` — pytest suite

## References

- Fluent Python, 2nd ed., Chapters 7 & 9
- Effective Python, 3rd ed., Items 26–32
