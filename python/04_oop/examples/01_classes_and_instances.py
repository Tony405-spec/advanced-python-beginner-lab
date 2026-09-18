"""Classes, instances, attributes, methods.

Run:
    python python/04_oop/examples/01_classes_and_instances.py
"""


class BankAccount:
    """A simple bank account with class and instance attributes."""

    # Class attribute — shared by all instances unless shadowed
    bank_name: str = "Python Bank"
    total_accounts: int = 0

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        # Instance attributes — unique per instance
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"


def main() -> None:
    print("=== Instances ===")
    a = BankAccount("Ada", 100)
    b = BankAccount("Grace")
    print(f"  a = {a}")
    print(f"  b = {b}")

    print("\n=== Methods ===")
    a.deposit(50)
    print(f"  after a.deposit(50): {a}")
    a.withdraw(30)
    print(f"  after a.withdraw(30): {a}")

    print("\n=== Class attribute ===")
    print(f"  BankAccount.bank_name = {BankAccount.bank_name!r}")
    print(f"  a.bank_name          = {a.bank_name!r}")
    print(f"  BankAccount.total_accounts = {BankAccount.total_accounts}")

    print("\n=== Error handling ===")
    try:
        b.withdraw(100)
    except ValueError as e:
        print(f"  b.withdraw(100) -> ValueError: {e}")


if __name__ == "__main__":
    main()
