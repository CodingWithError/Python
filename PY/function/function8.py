def Great(no1,no2,no3):
  if no1>no2 and no1>no3:
    return no1
  elif no2>no1 and no2>no3:
    return no2
  else:
    return no3

print(Great(3, 4, 1))
print(Great(99, -4, 7))
print(Great(0, 0, 0))