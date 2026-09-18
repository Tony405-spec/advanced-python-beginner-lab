# Module 05 — Modules and Packages

How Python finds, loads, and caches code. Imports, packages, `__init__.py`,
`__all__`, and the import system.

## Concepts covered

- **Modules** — a `.py` file is a module. Importing runs it once, caches it.
- **Packages** — a directory with `__init__.py` (or a namespace package).
- **`import` forms** — `import x`, `from x import y`, relative vs. absolute.
- **`__name__` and `if __name__ == "__main__"`**.
- **`__all__`** — controls `from module import *`.
- **The import cache** — `sys.modules`.
- **Circular imports** — why they happen, how to avoid them.

## References

- Python docs — Modules: https://docs.python.org/3/tutorial/modules.html
- Python docs — Import system: https://docs.python.org/3/reference/import.html
