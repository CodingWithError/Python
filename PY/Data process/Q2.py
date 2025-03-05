import urllib.request
import json

url="https://studies.cs.helsinki.fi/stats-mock/api/courses"
with urllib.request.urlopen(url) as resp:
  data=json.loads(resp.read().decode())

print(data)
print()
print()
def retrieve_All(data):
  Lis=[]
  for i in data:
    fullName=i["fullName"]
    name=i["name"]
    year=i["year"]
    exercises=0
    for j in i["exercises"]:
      exercises+=int(j)
    tup=(fullName,name,year,exercises)
    Lis.append(tup)
  return Lis

Lis=retrieve_All(data)
print(Lis)