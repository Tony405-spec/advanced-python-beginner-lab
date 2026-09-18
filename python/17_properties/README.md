# Module 17 — Properties

`@property` turns a method into an attribute. Access `obj.area` without
parentheses, get computed values, add validation to attribute assignment,
and keep your public API stable when internals change.

## Concepts covered

- **`@property`** — read-only computed attributes.
- **`@name.setter`** — validate or transform on assignment.
- **`@name.deleter`** — run code on `del obj.name`.
- **Caching with properties.**
- **Lazy initialization.**
- **Property vs. plain attribute vs. method — when to use which.**

## Data Science connection

A DataFrame class with `.shape` as a property, a trained model with
`.num_parameters` computed lazily, a dataset with `.mean` cached after
first access — properties keep the public API clean while hiding the
computation behind the scenes.

## References

- Python docs — property: https://docs.python.org/3/library/functions.html#property
- Fluent Python, 2nd ed., Chapter 22
