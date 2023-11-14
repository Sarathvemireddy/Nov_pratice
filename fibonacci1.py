def fib(n):
  if n < 0:
    raise ValueError("n must be a non-negative integer")
  elif n == 0 or n == 1:
    return n
  else:
    return fib(n - 1) + fib(n - 2)

def fib_sequence(n):
  return [fib(x) for x in range(n + 1)]
