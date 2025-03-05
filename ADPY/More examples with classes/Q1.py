class Item:
  def __init__(self,item: str,weight: int):
    self.__name=item
    self.__weight=weight

  def name(self):
    return self.__name
  
  def weight(self):
    return self.__weight
  
  def __str__(self):
    return f'{self.__name} ({self.__weight} kg)'


class Suitcase:
  def __init__(self,maxWeight: int):
    self.__maxWeight=maxWeight
    self.__items=[]
  
  def add_item(self,item):
    if self.total_weight()+item.weight()<=self.__maxWeight:
      self.__items.append(item)
  
  def total_weight(self):
    return sum(item.weight() for item in self.__items)

  def __str__(self):
    if len(self.__items)==1:
      return f'{len(self.__items)} item ({self.total_weight()} kg)'
    return f'{len(self.__items)} items ({self.total_weight()} kg)'

  def print_items(self):
    for i in self.__items:
      print(f'{i.name()} ({i.weight()} kg)')

  def weight(self):
    return self.total_weight()
  
  def heaviest_item(self):
    maxItemWeight=0
    itemName=''
    for i in self.__items:
      if i.weight()>maxItemWeight:
        itemName=i.name()
        maxItemWeight=i.weight()
    return f'{itemName} ({i.weight()} kg)'


class CargoHold:
  def __init__(self,max_weight):
    self.__maxWeight=max_weight
    self.__suitcases=[]

  def add_suitcase(self,suitcase):
    if self.__maxWeight>=suitcase.weight():
      self.__suitcases.append(suitcase)
      self.__maxWeight-=suitcase.weight()

  def __str__(self):
    if len(self.__suitcases)==1:
      return f"{len(self.__suitcases)} suitcase, space for {self.__maxWeight} kg"
    return f"{len(self.__suitcases)} suitcases, space for {self.__maxWeight} kg"

  def print_items(self):
    for i in self.__suitcases:
      if i.print_items()!=None:
        print(i.print_items())



book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()