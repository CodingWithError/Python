class ListHelper:

  @classmethod
  def greatest_frequency(cls,my_list: list):
    counts={}
    for i in my_list:
      counts[i]=counts.get(i,0)+1

    most_common=None
    highest=0
    for i ,count in counts.items():
      if count>highest:
        most_common=i
        highest=count
    
    return most_common

  @staticmethod
  def doubles(my_list: list):
    counts={}
    for i in my_list:
      counts[i]=counts.get(i,0)+1

    doubles=[]
    for i,count in counts.items():
      if count>=2:
        doubles.append(i)
    return len(doubles)
  
numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))

