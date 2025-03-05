class Clock:
  def __init__(self,hr: int,min: int,sec: int):
    self.hour=hr
    self.minutes=min
    self.seconds=sec
  
  def tick(self):
    self.seconds += 1
    if self.seconds == 60:  
      self.seconds = 0
      self.minutes += 1
      if self.minutes == 60:  
        self.minutes = 0
        self.hour += 1
        if self.hour == 24:  
          self.hour = 0

  def __str__(self):
    return f"{self.hour:02}:{self.minutes:02}:{self.seconds:02}" 
  
  def set(self,hr: int,min: int):
    self.hour = hr
    self.minutes = min
    self.seconds = 0


clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)