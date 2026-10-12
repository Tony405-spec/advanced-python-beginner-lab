"""Property-based testing with hypothesis.

Run:
    pip install hypothesis
    pytest python/24_testing/examples/03_property_based.py -v

Property-based tests describe INVARIANTS that must hold for all valid
inputs, and hypothesis generates hundreds of examples automatically —
including edge cases you'd never think to write.

This file is both runnable as a script and valid as a pytest suite.
"""

import pytest

try:
    from hypothesis import given, strategies as st, assume
    HAS_HYPOTHESIS = True
except ImportError:
    HAS_HYPOTHESIS = False


# ---------------------------------------------------------------
# Code under test
# ---------------------------------------------------------------

def encode(s: str) -> str:
    """Encode a string by prefixing length (a toy encoding)."""
    return f"{len(s)}:{s}"


def decode(s: str) -> str:
    """Decode the string produced by encode."""
    if ":" not in s:
        raise ValueError(f"malformed encoding: {s!r}")
    length_str, _, payload = s.partition(":")
    if not length_str.isdigit():
        raise ValueError(f"malformed length: {length_str!r}")
    length = int(length_str)
    if length != len(payload):
        raise ValueError(
            f"length mismatch: declared {length}, actual {len(payload)}"
        )
    return payload


def reverse(xs: list) -> list:
    """Return a new list in reverse order."""
    return xs[::-1]


def sort_ints(xs: list[int]) -> list[int]:
    """Return a sorted copy."""
    return sorted(xs)


# ---------------------------------------------------------------
# Example-based tests (what we've been writing all along)
# ---------------------------------------------------------------

def test_encode_example():
    assert encode("hello") == "5:hello"


def test_reverse_example():
    assert reverse([1, 2, 3]) == [3, 2, 1]


# ---------------------------------------------------------------
# Property-based tests: invariants that must hold for ALL inputs
# ---------------------------------------------------------------

@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
@given(st.text())
def test_encode_decode_roundtrip(s):
    """Property: decode(encode(s)) == s for any string."""
    assert decode(encode(s)) == s


@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
@given(st.lists(st.integers()))
def test_reverse_is_involution(xs):
    """Property: reversing twice returns the original."""
    assert reverse(reverse(xs)) == xs


@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
@given(st.lists(st.integers()))
def test_reverse_preserves_length(xs):
    """Property: reverse does not change length."""
    assert len(reverse(xs)) == len(xs)


@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
@given(st.lists(st.integers()))
def test_sort_is_idempotent(xs):
    """Property: sorting twice equals sorting once."""
    assert sort_ints(sort_ints(xs)) == sort_ints(xs)
