from datetime import date, timedelta

class SimpleDate:
  def __init__(self,day: int,month: int,year: int):
    self._day=day
    self._month=month
    self._year=year

  def __str__(self):
    return f"{self._day}.{self._month}.{self._year}"
  
  def __eq__(self, another):
    return self._day==another._day and self._month==another._month and self._year==another._year
  
  def __ne__(self, another):
    return not self.__eq__(another)
  
  def __lt__(self,another):
    return (self._day,self._month,self._year)>(another._day,another._month,another._year)
  
  def __gt__(self,another):
    return (self._day,self._month,self._year)<(another._day,another._month,another._year)

  def __add__(self,days: int):
    current_date = date(self._year, self._month, self._day)
    new_date = current_date + timedelta(days=days)

    return SimpleDate(new_date.day, new_date.month, new_date.year)
  def __sub__(self, another):
    self_days = self._year * 360 + self._month * 30 + self._day
    another_days = another._year * 360 + another._month * 30 + another._day

    return abs(self_days - another_days)  # Ensure positive difference

d1 = SimpleDate(4, 10, 2020)
d2 = SimpleDate(2, 11, 2020)
d3 = SimpleDate(28, 12, 1985)

print(d2-d1)
print(d1-d2)
print(d1-d3)