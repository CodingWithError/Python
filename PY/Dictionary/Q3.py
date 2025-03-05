def SS(S):
  dec={}
  for i in S:
    dec[i]=S.count(i)
  return dec
  
def Dis(name):
  Dir=SS(name)
  for i in Dir:
    print(f"{i} {Dir[i]*'*'}")
  
Dis("abba")
print()
Dis("statistically")