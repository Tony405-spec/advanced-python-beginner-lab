# Module 07 — Files and Serialization

Reading and writing files, plus the three formats every Data Scientist
works with: CSV, JSON, and (lightly) pickle.

## Concepts covered

- **Text vs. binary mode** — `"r"`, `"w"`, `"a"`, `"rb"`, `"wb"`.
- **Encoding** — always pass `encoding="utf-8"`.
- **Context managers** — `with open(...) as f:` (why you never forget to close).
- **Paths** — `pathlib.Path` over `os.path`.
- **CSV** — `csv` module for small files, `pandas` for big ones.
- **JSON** — `json` module, `load`/`dump` vs `loads`/`dumps`.
- **Pickle** — why it exists, why it's dangerous, when it's OK.

## Data Science connection

Almost every data pipeline starts with "read a file" and ends with
"write a file". Knowing how to do this safely — with explicit encoding,
correct modes, and context managers — avoids the most common pipeline
failures: encoding errors, half-written files, and resource leaks.

## References

- Python docs — Input and output: https://docs.python.org/3/tutorial/inputoutput.html
- Python docs — `pathlib`: https://docs.python.org/3/library/pathlib.html
