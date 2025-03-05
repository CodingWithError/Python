def shape(no,sym,no1,sym1):
  for i in range(1,no+1):
    for j in range(i):
      print(sym,end="")
    print()
  for k in range(no1):
    for l in range(no):
      print(sym1,end="")
    print()
    
shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")