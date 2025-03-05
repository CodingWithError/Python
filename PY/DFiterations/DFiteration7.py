def sum_list(list1,list2):
  mainlist=[]
  for i in range(len(list1)):
    mainlist.append(list1[i]+list2[i])
  return mainlist

a = [1, 2, 3]
b = [7, 8, 9]
print(sum_list(a, b))