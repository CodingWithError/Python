class MagicPotion:
  def __init__(self,name: str):
    self.name=name
    self.ingredients=[]

  def add_ingredients(self,ingredient: str,amount: str):
    self.ingredients.append((ingredient,amount))
  
  def print_recipe(self):
    print(f'{self.name}')
    for i,a in self.ingredients:
      print(f'{i} {a} grams')
  
class SecretMagicPotion(MagicPotion):
  def __init__(self,name: str,password: str):
    super().__init__(name)
    self._password=password
  
  def add_ingredient(self, ingredient: str, amount: float, password: str):
    if password != self._password:
      raise ValueError("Wrong password!")
    super().add_ingredient(ingredient, amount)
    
  def print_recipe(self, password: str):
    if password != self._password:
      raise ValueError("Wrong password!")
    super().print_recipe()
