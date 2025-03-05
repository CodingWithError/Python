class Present:
  def __init__(self,name: str,weight: int):
    self.name=name
    self.weight=weight

  def __str__(self):
    return f"{self.name} ({self.weight}Kg)"  

class Box:
  def __init__(self):
    self.items=[]
  
  def add_present(self,book: Present):
    self.items.append(book)

  def total_weight(self):
    return sum(present.weight for present in self.items)


book = Present("ABC Book", 2)

box = Box()
box.add_present(book)
print(box.total_weight())

cd = Present("Pink Floyd: Dark Side of the Moon", 1)
box.add_present(cd)
print(box.total_weight())
