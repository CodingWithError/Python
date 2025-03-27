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
  
e1 = Money(4, 10)
e2 = Money(2, 5)
e3 = Money(4, 10)

print(e1)
print(e2)
print(e3)
print(e1 == e2)
print(e1 == e3)