def long_len(list):
  LL=[]
  for i in list:
    LL.append(len(i))
  LL=sorted(LL)
  return LL[-1]

my_list = ["first", "second", "fourth", "eleventh"]

result = long_len(my_list)
print(result)