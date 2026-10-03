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
def temperature_band(temp_celsius: float) -> str:
    """Classify temperature into bands using guards."""
    match temp_celsius:
        case t if t < 0:
            return "freezing"
        case t if t < 15:
            return "cold"
        case t if t < 25:
            return "mild"
        case t if t < 35:
            return "warm"
        case _:
            return "hot"


def month_season(month: int) -> str:
    """Map month to season using OR patterns."""
    match month:
        case 12 | 1 | 2:
            return "winter"
        case 3 | 4 | 5:
            return "spring"
        case 6 | 7 | 8:
            return "summer"
        case 9 | 10 | 11:
            return "autumn"
        case _:
            return "invalid month"


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
       print("\n=== Temperature bands (guards) ===")
    for t in [-5, 10, 20, 30, 40]:
        print(f"  {t:>3}°C: {temperature_band(t)}")

    print("\n=== Month → season (OR patterns) ===")
    for m in [1, 4, 7, 10, 13]:
        print(f"  month {m:>2}: {month_season(m)}")

if __name__ == "__main__":
    main()
