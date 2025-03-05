def read_fruits():
  fruits={}
  try:
    with open("fruits1.csv","r") as file:
      for line in file:
        fruit, price=line.strip().split(";")
        fruits[fruit]=float(price)
  except FileNotFoundError:
    print("Error: file not fount")
  except ValueError:
    print("Error: Invalid data")
  return fruits

fruits = read_fruits()
print(fruits)