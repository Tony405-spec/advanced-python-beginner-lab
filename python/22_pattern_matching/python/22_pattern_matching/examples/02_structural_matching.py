"""Structural pattern matching — sequences, mappings, and class patterns.

Run:
    python python/22_pattern_matching/examples/02_structural_matching.py
"""

from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Circle:
    center: Point
    radius: float


def describe_point(p: Point) -> str:
    match p:
        case Point(x=0, y=0):
            return "origin"
        case Point(x=0, y=y):
            return f"on y-axis at y={y}"
        case Point(x=x, y=0):
            return f"on x-axis at x={x}"
        case Point(x=x, y=y) if x == y:
            return f"on diagonal at ({x}, {y})"
        case Point():
            return f"general point {p}"
        case _:
            return "not a point"


def describe_sequence(seq) -> str:
    match seq:
        case []:
            return "empty"
        case [single]:
            return f"one element: {single}"
        case [first, second]:
            return f"pair: {first}, {second}"
        case [first, *rest]:
            return f"head {first!r} + {len(rest)} tail items"
        case _:
            return "not a sequence"


def describe_mapping(data: dict) -> str:
    match data:
        case {"type": "user", "id": uid}:
            return f"user id={uid}"
        case {"type": "post", "author": author, "content": _}:
            return f"post by {author}"
        case {"type": "comment", "post_id": pid, "author": a}:
            return f"comment on post {pid} by {a}"
        case {"error": message}:
            return f"error: {message}"
        case {}:
            return "unknown mapping shape"
        case _:
            return "not a mapping"


def dispatch_event(event: dict) -> str:
    match event:
        case {"kind": "click", "position": Point(x=x, y=y)}:
            return f"click at ({x}, {y})"
        case {"kind": "keypress", "key": str() as k}:
            return f"key pressed: {k!r}"
        case {"kind": "scroll", "delta": int(d) | float(d)}:
            return f"scroll by {d}"
        case {"kind": kind}:
            return f"unknown event kind: {kind!r}"
        case _:
            return "malformed event"

def json_response_summary(response: dict) -> str:
    """Summarize a JSON-style API response using structural matching."""
    match response:
        case {"status": 200, "data": {"users": [*users]}}:
            return f"OK — {len(users)} users returned"
        case {"status": 200, "data": dict() as payload}:
            return f"OK — payload keys: {sorted(payload)}"
        case {"status": 404}:
            return "not found"
        case {"status": 500, "error": msg}:
            return f"server error: {msg}"
        case {"status": int(code)} if code >= 400:
            return f"client/server error {code}"
        case _:
            return "unrecognized response shape"


def classify_shape(shape) -> str:
    """Classify geometric shapes using nested class patterns."""
    match shape:
        case Circle(center=Point(x=0, y=0), radius=r):
            return f"circle centered at origin, radius={r}"
        case Circle(center=Point(x=x, y=y), radius=r):
            return f"circle at ({x}, {y}), radius={r}"
        case Point(x=x, y=y):
            return f"point ({x}, {y})"
        case _:
            return "unknown shape"
            
def main() -> None:
    print("=== Class patterns ===")
    for p in [Point(0, 0), Point(0, 5), Point(3, 0), Point(4, 4), Point(2, 7)]:
        print(f"  {p}: {describe_point(p)}")

    print("\n=== Sequence patterns ===")
    for seq in [[], [1], [1, 2], [1, 2, 3, 4], (10, 20, 30), "not a list"]:
        print(f"  {seq!r}: {describe_sequence(seq)}")

    print("\n=== Mapping patterns ===")
    payloads = [
        {"type": "user", "id": 42},
        {"type": "post", "author": "ada", "content": "hi"},
        {"type": "comment", "post_id": 7, "author": "grace"},
        {"error": "not found"},
        {"foo": "bar"},
    ]
    for payload in payloads:
        print(f"  {payload}: {describe_mapping(payload)}")

    print("\n=== Nested patterns ===")
    events = [
        {"kind": "click", "position": Point(3, 4)},
        {"kind": "keypress", "key": "Enter"},
        {"kind": "scroll", "delta": 100},
        {"kind": "hover"},
        "not a dict",
    ]
    for event in events:
        print(f"  {event}: {dispatch_event(event)}")

    print("\n=== JSON response summary ===")
    responses = [
        {"status": 200, "data": {"users": [{"id": 1}, {"id": 2}]}},
        {"status": 200, "data": {"count": 5, "page": 1}},
        {"status": 404},
        {"status": 500, "error": "db down"},
        {"status": 418},
        {"foo": "bar"},
    ]
    for response in responses:
        print(f"  {response}: {json_response_summary(response)}")

    print("\n=== Shape classification (nested class patterns) ===")
    shapes = [
        Circle(Point(0, 0), 5),
        Circle(Point(3, 4), 2),
        Point(7, 8),
        "not a shape",
    ]
    for shape in shapes:
        print(f"  {shape}: {classify_shape(shape)}")
        
if __name__ == "__main__":
    main()
