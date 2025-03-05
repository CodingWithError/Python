def no_vowels(string):
  vowels="aeiou"
  result=""

  for char in string:
    if char not in vowels:
      result+=char
  return result

my_string = "this is an example"
print(no_vowels(my_string))