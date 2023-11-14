def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
  print("Factorial does not exist for negative numbers.")
else:
  factorial_result = factorial(num)

  print("The factorial of", num, "is", factorial_result)
