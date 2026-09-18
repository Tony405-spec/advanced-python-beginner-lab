"""Functions are first-class objects in Python.

Run:
    python python/02_functions/examples/01_functions_are_objects.py
"""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}"


def apply_twice(func, value):
    """Call func twice on value."""
    return func(func(value))


def make_multiplier(factor: int):
    """Return a function that multiplies its input by factor."""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier


def main() -> None:
    print("=== Functions are objects ===")
    print(f"type(greet)       = {type(greet)}")
    print(f"greet.__name__    = {greet.__name__}")
    print(f"greet.__doc__     = {greet.__doc__!r}")
    print(f"greet.__module__  = {greet.__module__}")

    print("\n=== Assigning to another name ===")
    hi = greet
    print(f"hi is greet       = {hi is greet}")
    print(f"hi('Ada')         = {hi('Ada')!r}")

    print("\n=== Storing in a data structure ===")
    handlers = {"greeting": greet}
    print(f"handlers['greeting']('Grace') = {handlers['greeting']('Grace')!r}")

    print("\n=== Passing as an argument ===")
    print(f"apply_twice(str.upper, 'hi')  = {apply_twice(str.upper, 'hi')!r}")
    print(f"apply_twice(str.strip, '  x  ') = {apply_twice(str.strip, '  x  ')!r}")

    print("\n=== Returning from a function ===")
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"double(10)        = {double(10)}")
    print(f"triple(10)        = {triple(10)}")
    print(f"double.__name__   = {double.__name__!r}")
    print(f"double.__closure__[0].cell_contents = "
          f"{double.__closure__[0].cell_contents!r}")

    print("\n=== Adding attributes to a function ===")
    greet.version = "1.0"
    greet.author = "Tony405-spec"
    print(f"greet.version     = {greet.version!r}")
    print(f"greet.author      = {greet.author!r}")


if __name__ == "__main__":
    main()
