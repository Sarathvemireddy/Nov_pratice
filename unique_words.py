def print_unique_words(filename):
    
    with open(filename, 'r') as f:
        contents = f.read()

    words = contents.split()

    words = [word.lower() for word in words]

    unique_words = set()

    for word in words:
        unique_words.add(word)

    sorted_words = sorted(unique_words)

    for word in sorted_words:
        print(word)

filename = input("Enter the filename: ")

print_unique_words(filename)
