class Rectangle:
  def __init__(self,length: int,breath: int):
    self._length=length
    self._breath=breath

  def __str__(self):
    return f'rectangle {self._length}X{self._breath}'
  
  def area(self):
    return self._length*self._breath
  
class Square(Rectangle):
  def __init__(self,side: int):
    super().__init__(side,side)

  def __str__(self):
    return f'square {self._length}x{self._breath}'


square = Square(4)
print(square)
print("area:", square.area())