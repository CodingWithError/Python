def remove_min(number: list):
  smallest=min(number)
  number.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_min(numbers)
    print(numbers)





