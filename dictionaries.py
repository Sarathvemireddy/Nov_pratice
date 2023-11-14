# Demonstration working with dictionaries 
my_dict = {
  "name": "Nikhil",
  "age": 23,
  "occupation": "Associate Developer"
}

print(my_dict)

print(my_dict["name"])

my_dict["favorite_color"] = "black"

print(my_dict)

del my_dict["occupation"]

print(my_dict)

print("age" in my_dict)

for key, value in my_dict.items():
  print(f"{key}: {value}")
