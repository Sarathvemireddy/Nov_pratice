def convert_to_celsius(fahrenheit):

  celsius = (fahrenheit - 32) * 5 / 9
  return celsius


def convert_to_fahrenheit(celsius):
  
  fahrenheit = (celsius * 9 / 5) + 32
  return fahrenheit

print(convert_to_celsius(100))
print(convert_to_fahrenheit(0))
