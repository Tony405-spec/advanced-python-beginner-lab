"""Higher-order functions and lambdas in practice.

Run:
    python python/02_functions/examples/03_higher_order_and_lambdas.py
"""

from functools import reduce


def make_adder(n: int):
    """Return a function that adds n to its argument."""
    return lambda x: x + n


def compose(*functions):
    """Compose functions right-to-left: compose(f, g)(x) == f(g(x))."""
    def composed(x):
        for fn in reversed(functions):
            x = fn(x)
        return x
    return composed


def main() -> None:
    nums = [3, 1, 4, 1, 5, 9, 2, 6]

    print("=== map ===")
    squares = list(map(lambda x: x * x, nums))
    print(f"  squares = {squares}")

    print("\n=== filter ===")
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(f"  evens   = {evens}")

    print("\n=== sorted with key ===")
    words = ["banana", "pie", "Washington", "book"]
    by_len = sorted(words, key=len)
    print(f"  by length     = {by_len}")
    by_last = sorted(words, key=lambda w: w[-1])
    print(f"  by last char  = {by_last}")

    print("\n=== reduce ===")
    product = reduce(lambda a, b: a * b, nums, 1)
    print(f"  product = {product}")

    print("\n=== Closures returned by functions ===")
    add5 = make_adder(5)
    add10 = make_adder(10)
    print(f"  add5(1)  = {add5(1)}")
    print(f"  add10(1) = {add10(1)}")

    print("\n=== Function composition ===")
    pipeline = compose(str.strip, str.lower, lambda s: s.replace(" ", "-"))
    print(f"  pipeline('  Hello World  ') = {pipeline('  Hello World  ')!r}")

    print("\n=== When NOT to use a lambda ===")
    # Bad: unreadable, hard to test, no docstring
    bad = lambda x: x + 1 if x > 0 else x - 1
    # Good: named function
    def step(x: int) -> int:
        """Step positive numbers up, negative numbers down."""
        return x + 1 if x > 0 else x - 1
    print(f"  bad(5)  = {bad(5)}, good(5)  = {step(5)}")
    print(f"  bad(-5) = {bad(-5)}, good(-5) = {step(-5)}")


if __name__ == "__main__":
    main()
