def smallest_avg(person1: dict,person2: dict,person3: dict):
  def aveg(person):
    return (person["result1"]+person["result2"]+person["result3"])/3
  
  avg1=aveg(person1)
  avg2=aveg(person2)
  avg3=aveg(person3)

  smallest=min((avg1,person1),(avg2,person2),(avg3,person3))

  return smallest[1]

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_avg(person1, person2, person3))