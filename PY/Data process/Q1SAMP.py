import json

with open("Q1.json") as students:
  data=students.read()

Stu=json.loads(data)

for names in Stu:
  print(f"{names["name"]} {names["age"]} years ({names["hobbies"]})")