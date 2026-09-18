# Module 19 — Abstract Base Classes

ABCs define a contract: "any subclass must implement these methods."
They catch missing implementations at instantiation time rather than at
call time.

## Concepts covered

- **`abc.ABC`** and **`@abstractmethod`**.
- **Abstract properties** — `@property` + `@abstractmethod`.
- **`register()`** — virtual subclasses for external types.
- **`collections.abc`** — the standard ABCs (`Iterable`, `Sequence`, `Mapping`).
- **When to use ABCs vs. duck typing vs. Protocols (Module 20).**

## Data Science connection

`sklearn` uses ABCs for estimators (`BaseEstimator`), transformers
(`TransformerMixin`), and models. If you write custom transformers or
metrics, you subclass those ABCs. Understanding `collections.abc`
also explains why some "it looks like a list" objects don't behave
like lists.

## References

- Python docs — abc: https://docs.python.org/3/library/abc.html
- Python docs — collections.abc: https://docs.python.org/3/library/collections.abc.html
- Fluent Python, 2nd ed., Chapter 13
