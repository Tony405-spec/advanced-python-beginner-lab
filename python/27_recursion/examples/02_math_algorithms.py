# GCD, fibonacci, and Fast power
def gcd(a: int, b: int) -> int:
  """Euclid's algorithm for Greatest Common Divisor."""
  if a % b == 0:
    return b
  else:
    return gcd(b,a % b)

def fib (n: int) -> int:
  """Recursive Fibonacci sequence"""
  if n==1: return 0
  if n==2: return 1
  return fib(n-1) + fib(n-2)

def fpower(x: int, n: int) -> int:
  """Fast power algorithm: O(log n)."""
  if n == 0:
    return 1
  y = fpower(x, int(n/2))
  if n % 2 == 0:
    return y*Y
  return x*y*y
