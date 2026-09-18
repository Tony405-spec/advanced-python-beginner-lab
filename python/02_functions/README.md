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

### 1. Functions are objects

A `def` statement creates a function object and binds it to a name — exactly
like `x = 5` binds an int to a name. The function has a type, an identity, and
attributes.

    def greet(name):
        return f"Hello, {name}"

    print(type(greet))          # <class 'function'>
    print(greet.__name__)       # 'greet'
    print(greet.__doc__)        # None (no docstring)

    # Assign to another name — same object:
    hi = greet
    print(hi is greet)          # True

    # Store in a data structure:
    handlers = {"greeting": greet}
    handlers["greeting"]("Ada") # 'Hello, Ada'

### 2. Argument semantics

Python has four kinds of parameters:

- **Positional-only** — before a `/` marker. Callable only by position.
- **Positional-or-keyword** — normal parameters, can be passed either way.
- **Variadic positional** — `*args`, collects extra positional arguments as a tuple.
- **Keyword-only** — after a `*` marker, must be passed by keyword.
- **Variadic keyword** — `**kwargs`, collects extra keyword arguments as a dict.

Full order in a signature:

    def f(a, b, /, c, d, *args, e, f, **kwargs):
        ...

### 3. Higher-order functions

A higher-order function is one that takes a function as an argument or returns
a function. `map`, `filter`, `sorted(key=...)` are built-ins. You'll also write
your own.

### 4. Lambdas

A lambda is an expression that creates an anonymous function. It can only
contain a single expression (no statements). Use them for tiny inline
functions; avoid them when a `def` would be clearer.

### 5. `functools` (introduction)

`functools` provides tools built on the function-as-object model:

- `functools.partial` — partial application.
- `functools.reduce` — fold a sequence.
- `functools.lru_cache` — memoization (covered fully in Module 11).

## Data Science connection

- `pandas.apply` takes a function — you pass functions all the time.
- `sklearn` transformers and estimators are functions/objects composed together.
- Custom loss functions, feature transformations, and pipeline steps are all
  higher-order functions in practice.
- `functools.lru_cache` on an expensive feature-extraction function is one of
  the cheapest speedups available.

## Files in this module

- `examples/01_functions_are_objects.py` — demonstrate the object nature of functions.
- `examples/02_argument_semantics.py` — all parameter kinds in one file.
- `examples/03_higher_order_and_lambdas.py` — map, filter, sorted, closures-over-lambdas.
- `exercises/` — challenges.
- `tests/` — pytest suite.

## References

- Python docs — Function definitions: https://docs.python.org/3/reference/compound_stmts.html#function-definitions
- Python docs — `functools`: https://docs.python.org/3/library/functools.html
- Fluent Python, 2nd ed., Chapters 7 & 9 — Luciano Ramalho
- Effective Python, 3rd ed., Items 26–32 — Brett Slatkin
