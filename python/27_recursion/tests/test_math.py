import pytest
from examples.math_algorithms import gcd, fib, fpower

def test_gcd():
    assert gcd(6, 10) == 2
    assert gcd(10, 6) == 2

def test_fib():
    assert fib(1) == 0
    assert fib(6) == 5

def test_fpower():
    assert fpower(2, 3) == 8
    assert fpower(3, 4) == 81
