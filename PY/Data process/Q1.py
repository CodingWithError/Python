import json

def print_persons(file_name: str):
  with open(file_name) as students:
    data=json.load(students)

  for i in data:
    name=i["name"]
    age=i["age"]
    hobbies=",".join(i["hobbies"])
    print(f"{name} {age} years ({hobbies})")

print_persons("Q1.json")