"""Every parameter kind in Python, demonstrated in one file.

Run:
    python python/02_functions/examples/02_argument_semantics.py
"""


def positional_only(a, b, /):
    """a and b can ONLY be passed positionally."""
    return a + b


def keyword_only(*, a, b):
    """a and b can ONLY be passed by keyword."""
    return a + b


def mixed(a, b, /, c, d, *args, e, f, **kwargs):
    """Full signature with all five kinds of parameters."""
    return {
        "a": a, "b": b, "c": c, "d": d,
        "args": args,
        "e": e, "f": f,
        "kwargs": kwargs,
    }


def demo_args():
    """*args collects extra positional arguments as a tuple."""
    def total(*numbers):
        return sum(numbers)
    return total(1, 2, 3, 4, 5)


def demo_kwargs():
    """**kwargs collects extra keyword arguments as a dict."""
    def profile(**fields):
        return fields
    return profile(name="Ada", role="engineer", years=5)


def main() -> None:
    print("=== Positional-only (before /) ===")
    print(f"  positional_only(2, 3) = {positional_only(2, 3)}")
    try:
        positional_only(a=2, b=3)
    except TypeError as e:
        print(f"  positional_only(a=2, b=3) -> TypeError: {e}")

    print("\n=== Keyword-only (after *) ===")
    print(f"  keyword_only(a=2, b=3) = {keyword_only(a=2, b=3)}")
    try:
        keyword_only(2, 3)
    except TypeError as e:
        print(f"  keyword_only(2, 3) -> TypeError: {e}")

    print("\n=== Full mixed signature ===")
    result = mixed(1, 2, 3, 4, 5, 6, e=7, f=8, extra=9)
    for k, v in result.items():
        print(f"  {k:>7} = {v}")

    print("\n=== *args example ===")
    print(f"  total(1,2,3,4,5) = {demo_args()}")

    print("\n=== **kwargs example ===")
    print(f"  profile(...) = {demo_kwargs()}")

    print("\n=== Unpacking on the call side ===")
    nums = [1, 2, 3]
    print(f"  positional_only(*{nums}) = {positional_only(*nums)}")
    params = {"a": 10, "b": 20}
    print(f"  keyword_only(**{params}) = {keyword_only(**params)}")


if __name__ == "__main__":
    main()
