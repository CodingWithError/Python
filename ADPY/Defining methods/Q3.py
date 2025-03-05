class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value>0:
          self.value-=1

    def set_to_zero(self):
        self.value=0

counter = DecreasingCounter(100)
counter.print_value()
counter.set_to_zero()
counter.print_value()