def double(mylist: list):
  List=[]
  for i in mylist:
    List.append(i*2)
  return List


mylist=[2, 4, 5, 3, 11, -4]
DoubleList=double(mylist)

print(mylist)
print(DoubleList)