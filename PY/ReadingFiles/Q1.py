with open("numbers1.txt") as new_file:
  no=0
  for line in new_file:
    no=max(int(line),no)
  print(no)