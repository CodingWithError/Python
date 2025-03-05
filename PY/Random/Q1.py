from random import randint

def lottery_number(i1: int,i2: int,i3: int):
  Lis=[]
  for i in range(1,i1+1):
    Lis.append(randint(i2,i3))
  return Lis



Lis=lottery_number(7,1,40)
Lis.sort()
for i in Lis:
  print(i)