# Module 26 — Debugging

Writing code is half the job. Finding out why it doesn't work is the
other half. This module covers the tools Python gives you for
understanding failing code — from `print` to the debugger to
post-mortem inspection of crashes.

## Concepts covered

- **`print` debugging and its limits** — fine for tiny scripts, bad at scale.
- **`assert` statements** — invariants during development.
- **`logging` vs `print`** — the previous module's point, applied.
- **`breakpoint()` and `pdb`** — the built-in interactive debugger.
- **`pdb` commands** — `n`, `s`, `c`, `l`, `p`, `pp`, `w`, `q`.
- **Post-mortem debugging** — `pdb.pm()`, `python -m pdb`.
- **`traceback`** — reading and formatting stack traces.
- **`faulthandler`** — dump tracebacks on crash.
- **Debugging in notebooks** — `%debug`, `%%debug`.
- **Reproducing bugs** — minimal reproducible examples.

## Data Science connection

A pipeline crashes at 3 AM with a cryptic error. You need to know:
which function, which file, which row of data, what the state was.
Debugging discipline — combined with logging from Module 25 — is how
you turn "it crashed" into "here's the exact line and input".

## References

- Python docs — pdb: https://docs.python.org/3/library/pdb.html
- Python docs — traceback: https://docs.python.org/3/library/traceback.html
- Python docs — faulthandler: https://docs.python.org/3/library/faulthandler.html
