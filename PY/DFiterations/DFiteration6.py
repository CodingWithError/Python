def even_numbers(name):
  list=[]
  for i in name:
    if i%2==0:
      list.append(i)
  return list

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)
