
def fib(n):
  if n < 0:
    raise ValueError("n must be a non-negative integer")
  elif n == 0 or n == 1:
    return n
  else:
    return fib(n - 1) + fib(n - 2)

def fib_sequence(n):
  return [fib(x) for x in range(n + 1)]

import fibonacci

fib_5 = fibonacci.fib(5)

fib_sequence_10 = fibonacci.fib_sequence(10)
print(fib_sequence_10)
