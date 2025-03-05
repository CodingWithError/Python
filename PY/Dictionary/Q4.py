dir={}
while(True):
  no=int(input("command (1 search, 2 add, 3 quit): "))
  if no==3:
    print("quitting...")
    break
  elif no==2:
    name=str(input("name: "))
    num=int(input("number: "))
    print("ok!")
    dir[name]=num
  elif no==1:
    ng=str(input("name: "))
    print(dir[ng])
  else:
    print("wrong no")