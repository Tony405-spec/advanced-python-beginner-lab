"""Tower of Hanoi: The classic 3-step recursion strategy."""

def print_move(fr: str, to: str) -> None:
    print(f"Move from {fr} to {to}")

def towers(n: int, fr: str, to: str, spare: str) -> None:
    if n == 1:
        print_move(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)
