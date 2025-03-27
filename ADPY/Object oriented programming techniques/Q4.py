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
    return not self.__eq__(another)
  
  def __lt__(self, another):
    return (self._euros,self._cents)<(another._euros,another._cents)

  def __gt__(self, another):
    return (self._euros,self._cents)>(another._euros,another._cents)
  
  def __add__(self, another):
    totalCents=self._cents+another._cents
    extraEuros=totalCents//100
    new_cents=totalCents%100
    new_euros=self._euros+another._euros+extraEuros
    return Money(new_euros,new_cents)
 
  def __sub__(self, another):
    totalCents=self._euros*100+self._cents
    totalAnotherCents=another._euros*100+another._cents

    if totalCents<totalAnotherCents:
      raise ValueError("a negative result is not allowed")
   
    remaining_cents=totalCents-totalAnotherCents
    new_euros=remaining_cents//100
    new_cents=remaining_cents%100

    return Money(new_euros,new_cents)
  
e1 = Money(4, 5)
e2 = Money(2, 95)

e3 = e1 + e2
e4 = e1 - e2

print(e3)
print(e4)

e5 = e2-e1