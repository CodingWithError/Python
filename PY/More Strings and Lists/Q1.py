def everything_reversed(list):
  Lis=[]
  for i in list[::-1]:
    Lis.append(i[::-1])
  return Lis

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)