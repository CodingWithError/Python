class Present:
  def __init__(self,name: str,weight: int):
    self.name=name
    self.weight=weight

  def __str__(self):
    return f"{self.name} ({self.weight}Kg)"  


book = Present("ABC Book", 2)

print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print("Present:", book)

