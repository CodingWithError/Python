def time_ten(no,no1):
  direct={}
  for i in range(no,no1+1):
    direct[i]=i*10

  return direct

d=time_ten(3,6)
print(d)