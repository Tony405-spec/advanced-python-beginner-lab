"""map, filter, and reduce — the classic functional trio.

Run:
    python python/23_functional_programming/examples/01_map_filter_reduce.py
"""

from functools import reduce


def celsius_to_fahrenheit(c: float) -> float:
    """Pure function: Celsius -> Fahrenheit."""
    return c * 9 / 5 + 32


def is_even(n: int) -> bool:
    """Pure function: parity test."""
    return n % 2 == 0


def product(nums: list[int]) -> int:
    """Multiply a list of ints using reduce."""
    return reduce(lambda a, b: a * b, nums, 1)


def main() -> None:
    print("=== map: transform each item ===")
    celsius = [0, 10, 20, 30, 40]
    fahrenheit = list(map(celsius_to_fahrenheit, celsius))
    print(f"  celsius    = {celsius}")
    print(f"  fahrenheit = {fahrenheit}")

    print("\n=== filter: keep items matching a predicate ===")
    numbers = list(range(1, 11))
    evens = list(filter(is_even, numbers))
    print(f"  numbers = {numbers}")
    print(f"  evens   = {evens}")

    print("\n=== reduce: fold to a single value ===")
    print(f"  product([1, 2, 3, 4, 5]) = {product([1, 2, 3, 4, 5])}")

    print("\n=== Chaining map + filter ===")
    # Filter first (cheaper), then map.
    result = list(map(celsius_to_fahrenheit, filter(lambda c: c > 10, celsius)))
    print(f"  temps above 10C converted: {result}")

    print("\n=== Comprehensions vs functional style ===")
    # Same result, two styles.
    functional = list(map(celsius_to_fahrenheit, celsius))
    comprehension = [celsius_to_fahrenheit(c) for c in celsius]
    print(f"  map()           = {functional}")
    print(f"  comprehension   = {comprehension}")
    print("  (comprehension is usually more readable)")


if __name__ == "__main__":
    main()
