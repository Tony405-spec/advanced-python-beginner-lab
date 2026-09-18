"""Context managers: class-based and generator-based.

Run:
    python python/12_context_managers/examples/01_from_scratch.py
"""

import contextlib
import time


class Timer:
    """Class-based context manager that prints elapsed time."""

    def __init__(self, label: str = "block") -> None:
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"  [{self.label}] {elapsed:.6f}s")
        return False  # do not suppress exceptions


@contextlib.contextmanager
def timer(label: str = "block"):
    """Generator-based context manager — same behavior, less code."""
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"  [{label}] {elapsed:.6f}s")


def main() -> None:
    print("=== Class-based context manager ===")
    with Timer("sleep 0.05"):
        time.sleep(0.05)

    print("\n=== Generator-based context manager ===")
    with timer("sleep 0.05"):
        time.sleep(0.05)

    print("\n=== Cleanup runs even on exception ===")
    try:
        with Timer("raising block"):
            raise ValueError("boom")
    except ValueError as e:
        print(f"  caught: {e}")

    print("\n=== contextlib.suppress ===")
    with contextlib.suppress(FileNotFoundError):
        open("this-file-does-not-exist.txt")
    print("  no exception propagated — suppress worked")


if __name__ == "__main__":
    main()
