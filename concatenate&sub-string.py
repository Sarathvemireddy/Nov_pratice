def create_string(str1, str2):
 
  new_string = str1 + str2
  return new_string


def access_substring(str1, start_index, end_index):
  substring = str1[start_index:end_index]
  return substring


def main():


  str1 = "Hello"
  str2 = "World"

  new_string = create_string(str1, str2)

  print(new_string)

  substring = access_substring(new_string, 0, 5)

  print(substring)


if __name__ == "__main__":
  main()
