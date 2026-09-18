"""All four kinds of comprehension, plus when not to use them.

Run:
    python python/08_comprehensions/examples/01_all_kinds.py
"""

import sys


def main() -> None:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("=== List comprehension ===")
    squares = [n * n for n in nums]
    print(f"  squares       = {squares}")
    even_squares = [n * n for n in nums if n % 2 == 0]
    print(f"  even squares  = {even_squares}")

    print("\n=== Dict comprehension ===")
    word = "hello"
    letter_index = {ch: i for i, ch in enumerate(word)}
    print(f"  letter_index  = {letter_index}")
    price = {"apple": 1.2, "banana": 0.5, "cherry": 3.0}
    expensive = {k: v for k, v in price.items() if v > 1}
    print(f"  expensive     = {expensive}")

    print("\n=== Set comprehension ===")
    unique_lengths = {len(w) for w in ["hi", "hello", "hey", "world"]}
    print(f"  unique_lengths = {unique_lengths}")

    print("\n=== Generator expression ===")
    gen = (n * n for n in nums)
    print(f"  type(gen)     = {type(gen).__name__}")
    print(f"  next(gen)     = {next(gen)}")
    print(f"  next(gen)     = {next(gen)}")
    print(f"  memory of gen = {sys.getsizeof(gen)} bytes")
    list_comp = [n * n for n in nums]
    print(f"  memory of list= {sys.getsizeof(list_comp)} bytes")

    print("\n=== Nested comprehension (flatten) ===")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    print(f"  flat          = {flat}")

    print("\n=== Conditional expression inside ===")
    signs = ["pos" if n > 0 else "neg" for n in [-2, 3, -1, 4]]
    print(f"  signs         = {signs}")

    print("\n=== When NOT to use a comprehension ===")
    # This is valid but bad. Use a plain loop.
    ugly = [print(f"  side effect {n}") or n for n in range(3)]
    print(f"  (that printed side effects above; result = {ugly})")


if __name__ == "__main__":
    main()
