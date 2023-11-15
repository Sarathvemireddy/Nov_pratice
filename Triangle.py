def is_right_triangle(a, b, c):
 
  a, b, c = sorted([a, b, c])

  return c * c == a * a + b * b

a = float(input("Enter the length of the first side of the triangle: "))
b = float(input("Enter the length of the second side of the triangle: "))
c = float(input("Enter the length of the third side of the triangle: "))

if is_right_triangle(a, b, c):
  print("The triangle is a right triangle.")
else:
  print("The triangle is not a right triangle.")
