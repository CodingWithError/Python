def older_people(P,Y):
  older=[]
  for i in P:
    if i[1]<Y:
      older.append(i[0])
  return older


p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

older = older_people(people, 1979)
print(older)