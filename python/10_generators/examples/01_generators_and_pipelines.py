"""Generators: lazy evaluation and pipelines.

Run:
    python python/10_generators/examples/01_generators_and_pipelines.py
"""

import sys
from itertools import count, islice


def count_up_to(n: int):
    """Yield integers from 0 up to n-1."""
    for i in range(n):
        yield i


def squares(nums):
    """Yield the square of each input."""
    for n in nums:
        yield n * n


def evens(nums):
    """Yield only even numbers."""
    for n in nums:
        if n % 2 == 0:
            yield n


def infinite_counter():
    """Yield 0, 1, 2, 3, ... forever (do not call list() on this)."""
    n = 0
    while True:
        yield n
        n += 1


def demo_basic():
    print("=== Generator function ===")
    gen = count_up_to(3)
    print(f"  type(gen) = {type(gen).__name__}")
    for n in gen:
        print(f"  {n}")

    print("\n=== Infinite generator with islice ===")
    first_ten = list(islice(infinite_counter(), 10))
    print(f"  first 10: {first_ten}")

    print("\n=== itertools.count ===")
    first_five = list(islice(count(100, 5), 5))
    print(f"  count(100, 5) first 5: {first_five}")


def demo_pipeline():
    print("\n=== Pipeline: squares of even numbers < 10 ===")
    pipeline = evens(squares(count_up_to(10)))
    result = list(pipeline)
    print(f"  result = {result}")

    print("\n=== Memory: list vs generator ===")
    list_ver = [n * n for n in range(1_000_000)]
    gen_ver = (n * n for n in range(1_000_000))
    print(f"  list:      {sys.getsizeof(list_ver):>12,} bytes")
    print(f"  generator: {sys.getsizeof(gen_ver):>12,} bytes")


def demo_yield_from():
    print("\n=== yield from ===")

    def chain_up_to(n: int):
        for i in range(n):
            yield from count_up_to(i)

    print(f"  chain_up_to(4) = {list(chain_up_to(4))}")


if __name__ == "__main__":
    demo_basic()
    demo_pipeline()
    demo_yield_from()
