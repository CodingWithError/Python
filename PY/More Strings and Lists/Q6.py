def longestST(string):
  longest=""
  for i in string:
    if len(longest)<len(i):
      longest=i
  return longest

my_list = ["apple", "banana", "cherry", "watermelon"]
result = longestST(my_list)
print(result)