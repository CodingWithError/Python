class Money:
  def __init__(self,euros: int,cents: int):
    self._euros=euros
    self._cents=cents

  def __str__(self):
    if self._cents<10:
      return f'{self._euros}.0{self._cents} eur'
    return f'{self._euros}.{self._cents} eur'

e1 = Money(4, 10)
e2 = Money(2, 6)  # two euros and five cents

print(e1)
print(e2)