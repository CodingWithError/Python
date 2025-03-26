class SuperHero:
  def __init__(self,name: str,superpowers: str):
    self.name=name
    self.superpowers=superpowers

class SuperGroup:
  def __init__(self,name:str,location: str):
    self._name=name
    self._location=location
    self._members=[]
  
  def get_name(self):
    return self._name
  
  def get_location(self):
    return self._location
  
  def add_member(self,hero):
    self._members.append(hero)

  def print_group(self):
    print(f'{self._name},{self._location}')
    print("Members:")

    for m in self._members:
      print(f"{m.name}, superPower: {m.superpowers}")

superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
invisible = SuperHero("Invisible Inca", "Invisibility")
revengers = SuperGroup("Revengers", "Emerald City")

revengers.add_member(superperson)
revengers.add_member(invisible)
revengers.print_group()
