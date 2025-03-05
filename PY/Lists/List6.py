def rangeoflist(list):
  list=sorted(list)
  no1=list[0]
  no2=list.pop()
  return no2-no1

List=[1,3,2,4,6,5]
result=rangeoflist(List)
print(result)