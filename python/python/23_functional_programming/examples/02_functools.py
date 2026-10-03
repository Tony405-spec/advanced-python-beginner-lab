"""functools: partial, lru_cache, singledispatch.

Run:
    python python/23_functional_programming/examples/02_functools.py
"""

import time
from functools import lru_cache, partial, singledispatch


# ---------------------------------------------------------------
# partial: freeze some arguments of a function
# ---------------------------------------------------------------

def power(base: float, exponent: float) -> float:
    """Return base ** exponent."""
    return base ** exponent


square = partial(power, exponent=2)
cube = partial(power, exponent=3)


# ---------------------------------------------------------------
# lru_cache: memoize expensive pure functions
# ---------------------------------------------------------------

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Naive Fibonacci, but memoized."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def slow_square(n: int) -> int:
    """Deliberately slow; used to compare timing with/without cache."""
    time.sleep(0.001)
    return n * n


@lru_cache(maxsize=128)
def cached_square(n: int) -> int:
    return slow_square(n)


# ---------------------------------------------------------------
# singledispatch: overload by first argument's type
# ---------------------------------------------------------------

@singledispatch
def describe(value) -> str:
    """Fallback for unknown types."""
    return f"unknown type: {type(value).__name__}"
@describe.register
def _(value: dict) -> str:
    return f"dict with keys {sorted(value)}"


def make_scaler(mean: float, std: float):
    """Return a partial that standardizes a single value.

    Useful for feature pipelines: fit once, apply many times.
    """
    def _standardize(x: float, *, mean: float, std: float) -> float:
        return (x - mean) / std
    return partial(_standardize, mean=mean, std=std)


@lru_cache(maxsize=256)
def expensive_feature(name: str, window: int) -> float:
    """Pretend to compute a rolling feature; cached for reuse."""
    time.sleep(0.001)
    return float(len(name) * window) / 10.0


@describe.register
def _(value: int) -> str:
    return f"integer: {value}"


@describe.register
def _(value: str) -> str:
    return f"string of length {len(value)}"


@describe.register
def _(value: list) -> str:
    return f"list with {len(value)} items"


def main() -> None:
    print("=== partial ===")
    print(f"  square(5) = {square(5)}")
    print(f"  cube(3)   = {cube(3)}")
    print(f"  square is a partial of power: {square.func is power}")
    print(f"  square.keywords           = {square.keywords}")

    print("\n=== lru_cache: Fibonacci ===")
    for n in [10, 50, 100]:
        t0 = time.perf_counter()
        value = fib(n)
        elapsed = time.perf_counter() - t0
        print(f"  fib({n:>3}) = {value}  ({elapsed:.6f}s)")
    print(f"  cache info: {fib.cache_info()}")

    print("\n=== lru_cache: caching a slow function ===")
    # First call (uncached) times 100 distinct values
    t0 = time.perf_counter()
    for n in range(100):
        cached_square(n)
    first_pass = time.perf_counter() - t0

    # Second pass hits the cache
    t0 = time.perf_counter()
    for n in range(100):
        cached_square(n)
    second_pass = time.perf_counter() - t0

    print(f"  first pass (cold): {first_pass:.4f}s")
    print(f"  second pass (hot): {second_pass:.4f}s")
    print(f"  cache info: {cached_square.cache_info()}")

    print("\n=== singledispatch ===")
    for value in [42, "hello", [1, 2, 3], 3.14, None]:
        print(f"  {value!r:>10} -> {describe(value)}")
        print("\n=== singledispatch with dict support ===")
    print(f"  {{'a': 1, 'b': 2}} -> {describe({'a': 1, 'b': 2})}")

    print("\n=== Feature pipeline: partial for standardization ===")
    scaler = make_scaler(mean=100.0, std=15.0)
    raw_values = [85, 100, 115, 130]
    standardized = [scaler(v) for v in raw_values]
    print(f"  raw          = {raw_values}")
    print(f"  standardized = {[round(s, 3) for s in standardized]}")

    print("\n=== Cached feature extraction ===")
    t0 = time.perf_counter()
    for _ in range(50):
        expensive_feature("age", 30)
    cold = time.perf_counter() - t0

    t0 = time.perf_counter()
    for _ in range(50):
        expensive_feature("age", 30)
    hot = time.perf_counter() - t0

    print(f"  cold: {cold:.4f}s, hot: {hot:.4f}s")
    print(f"  cache info: {expensive_feature.cache_info()}")


if __name__ == "__main__":
    main()
