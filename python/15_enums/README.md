# Module 15 — Enums

An enum is a fixed set of named values. `Color.RED` is clearer than `1`
and safer than a plain string. Enums prevent typos, enable IDE completion,
and make code self-documenting.

## Concepts covered

- **`Enum`** — basic named constants.
- **`IntEnum`** — enum members that are also ints.
- **`StrEnum`** (3.11+) — enum members that are also strings.
- **`auto()`** — automatic values.
- **`@unique`** — reject duplicate values.
- **`Flag`** — combinable bit flags.
- **Methods and properties on enums.**
- **Using enums in `match` statements (Module 22 preview).**

## Data Science connection

Feature types, model stages (`TRAIN`, `VALIDATE`, `TEST`), API status
codes, categorical encodings — anywhere you currently write `if status
== "training"`, an enum removes a class of bugs.

## References

- Python docs — enum: https://docs.python.org/3/library/enum.html
- Fluent Python, 2nd ed., Chapter 22
