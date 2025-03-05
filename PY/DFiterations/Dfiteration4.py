def palindromes(name):
  return name==name[::-1]

name=str(input())
if palindromes(name):
  print(f"{name} is a palindrome!")
else:
  print("that wasn't a palindrome")