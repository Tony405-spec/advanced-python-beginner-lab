"""Custom iterators and the iterator protocol.

Run:
    python python/09_iterators/examples/01_custom_iterator.py
"""


class Countdown:
    """Iterator that counts down from n to 1, then stops."""

    def __init__(self, start: int) -> None:
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


class CountdownReusable:
    """Iterable (not iterator) — each __iter__ returns a fresh iterator."""

    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self):
        return Countdown(self.start)


def main() -> None:
    print("=== Custom iterator ===")
    for n in Countdown(3):
        print(f"  {n}")

    print("\n=== Iterator is exhausted after one pass ===")
    c = Countdown(3)
    print(f"  first pass:  {list(c)}")
    print(f"  second pass: {list(c)}")

    print("\n=== Reusable iterable ===")
    r = CountdownReusable(3)
    print(f"  first pass:  {list(r)}")
    print(f"  second pass: {list(r)}")

    print("\n=== The `for` loop desugared ===")
    it = iter(Countdown(2))
    while True:
        try:
            value = next(it)
        except StopIteration:
            print("  StopIteration raised — loop would end here")
            break
        print(f"  {value}")

    print("\n=== iter() with sentinel ===")
    import random
    random.seed(42)
    rolls = iter(lambda: random.randint(1, 6), 6)
    print(f"  rolls until first 6: {list(rolls)}")


if __name__ == "__main__":
    main()
