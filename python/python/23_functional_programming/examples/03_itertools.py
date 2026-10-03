"""itertools: chain, groupby, product, combinations, permutations.

Run:
    python python/23_functional_programming/examples/03_itertools.py
"""

from itertools import (
    accumulate,
    chain,
    combinations,
    compress,
    count,
    dropwhile,
    groupby,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)

def moving_totals(values: list[float]) -> list[float]:
    """Cumulative sum — handy for running totals in feature engineering."""
    return list(accumulate(values))


def running_max(values: list[float]) -> list[float]:
    """Cumulative max — running high-water mark."""
    import operator
    return list(accumulate(values, func=operator.max))


def lazy_batches(data, batch_size: int):
    """Yield successive batches from any iterable — classic mini-batching."""
    it = iter(data)
    while True:
        batch = list(islice(it, batch_size))
        if not batch:
            return
        yield batch
        
def main() -> None:
    print("=== chain: glue multiple iterables ===")
    a = [1, 2, 3]
    b = (10, 20)
    c = range(100, 103)
    print(f"  chain(a, b, c) = {list(chain(a, b, c))}")

    print("\n=== count + islice ===")
    print(f"  first 5 of count(10, 2) = {list(islice(count(10, 2), 5))}")

    print("\n=== repeat ===")
    print(f"  repeat('x', 4) = {list(repeat('x', 4))}")

    print("\n=== product: cartesian product ===")
    colors = ["red", "green"]
    sizes = ["S", "M", "L"]
    for combo in product(colors, sizes):
        print(f"  {combo}")

    print("\n=== Hyperparameter grid (product of three lists) ===")
    lr = [0.01, 0.1]
    batch = [16, 32]
    dropout = [0.0, 0.5]
    grid = list(product(lr, batch, dropout))
    print(f"  grid size: {len(grid)}")
    for l, b, d in grid:
        print(f"    lr={l}, batch={b}, dropout={d}")

    print("\n=== groupby ===")
    data = [
        ("fruit", "apple"),
        ("fruit", "banana"),
        ("veg", "carrot"),
        ("veg", "kale"),
        ("fruit", "cherry"),
    ]
    # groupby requires the input to be sorted by the key
    data.sort(key=lambda x: x[0])
    for key, group in groupby(data, key=lambda x: x[0]):
        items = [v for _, v in group]
        print(f"  {key}: {items}")

    print("\n=== combinations vs permutations ===")
    pool = "ABC"
    print(f"  combinations('ABC', 2) = {list(combinations(pool, 2))}")
    print(f"  permutations('ABC', 2) = {list(permutations(pool, 2))}")

        print("\n=== accumulate: running totals and running max ===")
    prices = [100.0, 105.0, 98.0, 110.0, 92.0]
    print(f"  prices        = {prices}")
    print(f"  running total = {moving_totals(prices)}")
    print(f"  running max   = {running_max(prices)}")

    print("\n=== takewhile and dropwhile ===")
    seq = [1, 2, 3, 10, 4, 5]
    print(f"  takewhile(<5) = {list(takewhile(lambda x: x < 5, seq))}")
    print(f"  dropwhile(<5) = {list(dropwhile(lambda x: x < 5, seq))}")

    print("\n=== compress: keep by boolean mask ===")
    values = ["a", "b", "c", "d"]
    mask = [True, False, True, False]
    print(f"  compress = {list(compress(values, mask))}")

    print("\n=== lazy mini-batching ===")
    for i, batch in enumerate(lazy_batches(range(1, 11), batch_size=3)):
        print(f"  batch {i}: {batch}")
if __name__ == "__main__":
    main()
