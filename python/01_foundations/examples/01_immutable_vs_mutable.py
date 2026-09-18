"""Demonstration: names vs objects, identity vs equality, mutability,
truthiness, and the default-argument trap.

Run:
    python python/01_foundations/examples/01_immutable_vs_mutable.py
"""


def demo_immutability() -> None:
    """Integers and strings are immutable: rebinding a name creates a new object."""
    print("=== Immutability ===")

    a = 5
    b = a
    print(f"id(a) = {id(a)}, id(b) = {id(b)}  (same object)")
    a = a + 1  # rebinding, NOT mutation — creates a new int object
    print(f"after a = a + 1:")
    print(f"  a = {a}, b = {b}")
    print(f"  id(a) = {id(a)} (different), id(b) = {id(b)} (unchanged)")

    s = "hello"
    s2 = s
    s = s.upper()  # strings are immutable — this creates a new str
    print(f"  s = {s!r}, s2 = {s2!r}  (s2 unchanged)")


def demo_mutability() -> None:
    """Lists are mutable: methods change the object in place, and all
    names pointing at it see the change."""
    print("\n=== Mutability ===")

    lst = [1, 2, 3]
    alias = lst  # SAME object, second name
    lst.append(4)
    print(f"  lst   = {lst}")
    print(f"  alias = {alias}")
    print(f"  lst is alias -> {lst is alias}")

    # To get an independent copy:
    copy = lst.copy()
    lst.append(5)
    print(f"  after lst.append(5):")
    print(f"    lst  = {lst}")
    print(f"    copy = {copy}  (unaffected)")


def demo_identity_vs_equality() -> None:
    """`is` checks identity; `==` checks value equality."""
    print("\n=== Identity vs. equality ===")

    a = [1, 2, 3]
    b = [1, 2, 3]
    print(f"  a == b -> {a == b}   (same values)")
    print(f"  a is b -> {a is b}   (different objects)")

    # Small integers and short strings are interned by CPython.
    x = 256
    y = 256
    print(f"  256 is 256 (in same code object) -> {x is y}  (interned)")

    # None, True, False are singletons — `is` is the right check.
    val = None
    print(f"  val is None -> {val is None}   (correct pattern)")
    print(f"  val == None -> {val == None}   (works but is an anti-pattern)")


def demo_truthiness() -> None:
    """Every object has a truth value. Know the falsy ones."""
    print("\n=== Truthiness ===")

    falsy_values = [None, False, 0, 0.0, 0j, "", [], {}, set(), ()]
    for v in falsy_values:
        print(f"  bool({v!r:>8}) -> {bool(v)}")

    # Pitfall: custom objects can control truthiness.
    class Empty:
        def __bool__(self) -> bool:
            return False

    print(f"  bool(Empty()) -> {bool(Empty())}  (via __bool__)")


def demo_default_arg_trap() -> None:
    """Classic bug: mutable default arguments are shared across calls."""
    print("\n=== Default argument trap ===")

    def buggy_add(item, bucket=[]):
        bucket.append(item)
        return bucket

    print(f"  buggy_add(1) -> {buggy_add(1)}")
    print(f"  buggy_add(2) -> {buggy_add(2)}   <- surprise: [1, 2]")
    print(f"  buggy_add(3) -> {buggy_add(3)}")

    def correct_add(item, bucket=None):
        if bucket is None:
            bucket = []
        bucket.append(item)
        return bucket

    print(f"  correct_add(1) -> {correct_add(1)}")
    print(f"  correct_add(2) -> {correct_add(2)}   <- correct: [2]")


def main() -> None:
    demo_immutability()
    demo_mutability()
    demo_identity_vs_equality()
    demo_truthiness()
    demo_default_arg_trap()


if __name__ == "__main__":
    main()
