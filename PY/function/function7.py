def spruce(no):
  for i in range(no):
    space=no-i-1
    stars=2*i+1
    print(" " * space + "*" * stars)
  print(" " * (no - 1) + "*")


spruce(3)
print()
spruce(5)