# demonstration of working with tuples
my_tuple = ("apple", "banana", "cherry")

print(my_tuple)

print(my_tuple[1])

for item in my_tuple:
    print(item)

if "banana" in my_tuple:
    print("banana exists in the tuple")
else:
    print("banana does not exist in the tuple")

print(len(my_tuple))

another_tuple = ("orange", "grape", "watermelon")
combined_tuple = my_tuple + another_tuple
print(combined_tuple)

del my_tuple
