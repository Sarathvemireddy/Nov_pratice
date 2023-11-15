class StringReverser:
    def __init__(self):
        pass

    @staticmethod
    def reverse_words(input_string):
      
        words = input_string.split()

        reversed_words = words[::-1]

        reversed_string = ' '.join(reversed_words)

        return reversed_string

input_string = "This is a test string"
reverser = StringReverser()
result = reverser.reverse_words(input_string)
print(result)
