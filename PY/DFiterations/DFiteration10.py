def long_len(list):
  return min(list,key=len)

my_list = ["first", "second", "fourth", "eleventh"]

result = long_len(my_list)
print(result)