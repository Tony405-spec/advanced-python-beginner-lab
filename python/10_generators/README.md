# Module 10 — Generators

A generator is a function that produces values lazily using `yield`.
Generators are the single most important memory tool in Python.

## Concepts covered

- **`yield`** — pause a function, resume later.
- **Generator functions vs. generator expressions.**
- **Lazy evaluation** — compute only what you consume.
- **Pipelines** — chaining generators to process data in stages.
- **`yield from`** — delegate to a sub-generator.
- **`send()`, `throw()`, `close()`** — coroutine-style generators.
- **Infinite generators** — `itertools.count` style.

## Data Science connection

Reading a 50 GB CSV line by line, batching records for an API, streaming
training data into a model — all generators. Whenever you'd otherwise
load everything into memory, a generator lets you process it one item at
a time.

## References

- Python docs — Generators: https://docs.python.org/3/tutorial/classes.html#generators
- Fluent Python, 2nd ed., Chapter 17
- Effective Python, 3rd ed., Items 30–31
