"""Core data structures in Python: list, tuple, set, dict.

Run:
    python python/03_data_structures/examples/01_core_structures.py
"""

from collections import Counter, defaultdict


def demo_list() -> None:
    print("=== List (dynamic array) ===")
    xs = [1, 2, 3]
    xs.append(4)
    xs.insert(0, 0)
    print(f"  after append + insert: {xs}")
    print(f"  xs[0]  = {xs[0]}, xs[-1] = {xs[-1]}")
    print(f"  xs[1:3] = {xs[1:3]}")


def demo_tuple() -> None:
    print("\n=== Tuple (immutable) ===")
    point = (3, 4)
    x, y = point  # unpacking
    print(f"  point = {point}, x = {x}, y = {y}")
    try:
        point[0] = 99
    except TypeError as e:
        print(f"  point[0] = 99 -> TypeError: {e}")


def demo_set() -> None:
    print("\n=== Set (hash set) ===")
    a = {1, 2, 3}
    b = {3, 4, 5}
    print(f"  a | b = {a | b}  (union)")
    print(f"  a & b = {a & b}  (intersection)")
    print(f"  a - b = {a - b}  (difference)")
    print(f"  3 in a -> {3 in a}")


def demo_dict() -> None:
    print("\n=== Dict (hash map, insertion-ordered) ===")
    d = {"a": 1, "b": 2}
    d["c"] = 3
    print(f"  keys   = {list(d)}")
    print(f"  values = {list(d.values())}")
    print(f"  items  = {list(d.items())}")
    for k, v in d.items():
        print(f"    {k} -> {v}")


def demo_counter() -> None:
    print("\n=== Counter (from collections) ===")
    words = "the quick brown fox jumps over the lazy dog the".split()
    counts = Counter(words)
    print(f"  most common 3 = {counts.most_common(3)}")


def demo_defaultdict() -> None:
    print("\n=== defaultdict (from collections) ===")
    groups = defaultdict(list)
    for name in ["Ada", "Bob", "Alice", "Bill", "Cara"]:
        groups[name[0]].append(name)
    for letter, names in sorted(groups.items()):
        print(f"  {letter}: {names}")


def main() -> None:
    demo_list()
    demo_tuple()
    demo_set()
    demo_dict()
    demo_counter()
    demo_defaultdict()


if __name__ == "__main__":
    main()
