list=[]
while True:
  no=int(input("New item: "))
  if no==0:
    break
  list.append(no)
  print("List now: ", list)
  print("List inorder: ", sorted(list))

