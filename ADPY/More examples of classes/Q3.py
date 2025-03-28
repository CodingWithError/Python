class LunchCard:
  def __init__(self, balance: float):
    self.balance = balance

  def deposit_money(self,mon: int):
    if mon>0:
      self.balance+=mon

  def eat_lunch(self):
    self.balance-=2.60

  def eat_special(self):
    self.balance-=4.60

  def __str__(self):
    return f'The balance is {self.balance:.1f} euros'
  
peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f"Peter: {peters_card}")
print(f"Graces: {graces_card}")
peters_card.deposit_money(20)
graces_card.eat_special()
print(f"Peter: {peters_card}")
print(f"Graces: {graces_card}")
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f"Peter: {peters_card}")
print(f"Graces: {graces_card}")