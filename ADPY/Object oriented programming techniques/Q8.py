class ShoppingList():
  def __init__(self):
    self._items=[]

  def add(self,item: str,units: int):
    self._items.append((item,units))
  
  def __iter__(self):
     return iter(self._items)


shopping_list = ShoppingList()
shopping_list.add("bananas", 10)
shopping_list.add("apples", 5)
shopping_list.add("pineapple", 1)

for product in shopping_list:
    print(f"{product[0]}: {product[1]} units")