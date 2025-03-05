def sum_of_positives(name):
  sum=0
  for i in name:
    if i>0:
      sum+=i
  return sum

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)
