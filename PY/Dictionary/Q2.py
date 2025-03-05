def fac(no):
  ans=1
  for i in range(no,0,-1):
    ans=ans*i
  return ans

def dicFac(no):
  dic={}
  for i in range(no,0,-1):
    dic[i]=fac(i)
  return dic

k=dicFac(5)
print(k[1])
print(k[3])
print(k[5])