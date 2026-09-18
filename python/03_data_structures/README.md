# Module 03 — Data Structures

Lists, tuples, dicts, sets — and the deeper mechanics: hashing, ordering,
complexity, and how to pick the right structure for the job.

## Concepts covered

- **Lists** — dynamic arrays. Amortized O(1) append. O(n) insert/delete.
- **Tuples** — immutable sequences. Used for fixed-shape records.
- **Dicts** — hash maps. O(1) average lookup. Insertion-ordered since 3.7.
- **Sets** — hash sets. O(1) membership. Useful for dedup and algebra.
- **Hashing** — what makes dict/set possible. `__hash__` and `__eq__`.
- **Complexity** — big-O for the common operations.
- **Choosing a structure** — list vs. dict vs. set vs. tuple.

## Data Science connection

`groupby` uses dicts. Deduplication uses sets. Pipeline configuration is a
dict. Sparse feature vectors are often dicts of index → value. Understanding
these under the hood makes you faster with pandas, numpy, and sklearn.

## References

- Python docs — Data structures: https://docs.python.org/3/tutorial/datastructures.html
- Fluent Python, 2nd ed., Chapters 2–3
