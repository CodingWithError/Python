def oldest_person(people):
  old=people[0]
  for i in people:
    if i[1]<old[1]:
      old=i
  return old[0]

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))