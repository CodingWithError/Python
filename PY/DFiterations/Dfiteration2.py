def list_of_stars(list):
  for i in list:
    for j in range(i):
      print("*",end="")
    print()

List=[3, 7, 1, 1, 2]

list_of_stars(List)