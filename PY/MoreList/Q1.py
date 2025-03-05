def Count(m,no):
  count=0
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j]==no:
        count+=1
  return count


m = [[1, 2, 1], [0, 3, 4], [1, 0, 1]]
print(Count(m, 1))