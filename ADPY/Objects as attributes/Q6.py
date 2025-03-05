class Person:
  def __init__(self,name: str,height: int):
    self.name=name
    self.height=height

class Room:
  def __init__(self):
    self.group=[]
    self.SumHeight=0
  
  def add(self,person: Person):
    self.SumHeight+=person.height
    self.group.append(person)


  def is_empty(self):
    return len(self.group)==0
  
  def print_contents(self):
    print(f'There are {len(self.group)} persons in the room, and their combined height is {self.SumHeight} cm')
    for i in self.group:
      print(f'{i.name} ({i.height} cm)')

  def shortest(self):
    if self.is_empty():
      return None

    shortest=min(self.group,key=lambda person: person.height)
    return shortest

  def remove_shortest(self):
    shortPerson=self.shortest()
    if shortPerson:
      self.group.remove(shortPerson)
      self.SumHeight -= shortPerson.height
    return shortPerson
  

room = Room()

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))
room.print_contents()

print()

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")

print()

room.print_contents()