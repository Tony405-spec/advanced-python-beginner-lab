"""Basic pattern matching — literals, capture, wildcard, OR, guards.

Run:
    python python/22_pattern_matching/examples/01_basics.py
"""


def http_status_message(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 301 | 302:
            return "Redirect"
        case 400:
            return "Bad Request"
        case 401 | 403:
            return "Unauthorized or Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown"


def classify_number(n: int | float) -> str:
    match n:
        case 0:
            return "zero"
        case int() if n < 0:
            return "negative int"
        case int() if n > 0:
            return "positive int"
        case float() if n < 0:
            return "negative float"
        case float():
            return "non-negative float"
        case _:
            return "not a number"


def parse_command(command: str) -> str:
    match command.lower().strip():
        case "quit" | "exit" | "q":
            return "shutting down"
        case "help" | "h" | "?":
            return "showing help"
        case "":
            return "empty command"
        case other:
            return f"unknown command: {other!r}"


def main() -> None:
    print("=== HTTP status ===")
    for code in [200, 201, 301, 302, 400, 401, 403, 404, 500, 418]:
        print(f"  {code}: {http_status_message(code)}")

    print("\n=== Number classification ===")
    for value in [0, 5, -5, 3.14, -2.5, "hello"]:
        print(f"  {value!r:>8}: {classify_number(value)}")

    print("\n=== Command parsing (OR + capture patterns) ===")
    for cmd in ["quit", "EXIT", "  h  ", "", "deploy"]:
        print(f"  {cmd!r:>8}: {parse_command(cmd)}")


if __name__ == "__main__":
    main()
