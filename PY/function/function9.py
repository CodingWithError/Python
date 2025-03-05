def check(name,index1,index2):
  if index1<0 or index1>=len(name) or index2<0 or index2>=len(name):
    return False
  return name[index1]==name[index2]

print(check("programmer", 6, 7))
print(check("programmer", 0, 4))
print(check("programmer", 0, 12))