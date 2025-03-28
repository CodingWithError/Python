class Money:
  def __init__(self,euros: int,cents: int):
    self._euros=euros
    self._cents=cents

  def __str__(self):
    if self._cents<10:
      return f'{self._euros}.0{self._cents} eur'
    return f'{self._euros}.{self._cents} eur'
  
  def __eq__(self, another):
    return self._euros==another._euros and self._cents==another._cents
  
  def __ne__(self, another):
    return self._euros!=another._euros and self._cents!=another._cents
  
  def __lt__(self, another):
    return self._euros<another._euros and self._cents<another._cents

  def __gt__(self, another):
    return self._euros>another._euros and self._cents>another._cents

e1 = Money(4, 10)
e2 = Money(2, 5)

print(e1 != e2)
print(e1 < e2)
print(e1 > e2)