# Basic recursive functions:Factorial and Multiplication.
def factorial(n:int) -> int:
  """Completer n! using recursion."""
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
def mult(a: int, b: int) -> int:
  """Multiply a *b recursively by adding 'a' itself 'b' times."""
  if b == 1:
    return a
  else:
    return a+ mult(a,b-1)
