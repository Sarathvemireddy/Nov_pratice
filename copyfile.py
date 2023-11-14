# Prompt the user for the names of the source and destination files
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

# Open the source file in read mode
with open(source_file, "r") as source:
    # Read the contents of the source file
    contents = source.read()

# Open the destination file in write mode
with open(destination_file, "w") as destination:
    # Write the contents of the source file to the destination file
    destination.write(contents)

# Print a message indicating that the file has been copied
print("The contents of", source_file, "have been copied to", destination_file)
