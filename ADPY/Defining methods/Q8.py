class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count=0

    def add_number(self, number:int):
        self.numbers+=number
        self.count+=1

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return self.numbers
    
    def average(self):
        if self.count == 0:
            return 0
        return (self.numbers/self.count)
  
print('Please type in integer numbers:')
No=NumberStats()
while True:
    a=int(input())
    if a==-1:
        break
    No.add_number(a)

print("Sum of numbers:",No.get_sum())
print("Mean of numbers:",No.average())