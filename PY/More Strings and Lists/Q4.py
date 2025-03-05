def short(ls):
  short=[]
  for i in ls:
    if not i.isupper():
      short.append(i)
  return short

my_list=["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]

SH=short(my_list)
print(SH)