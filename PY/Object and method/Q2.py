def rowSum(mat):
  matri=[]
  for i in mat:
    row=i
    sum=0
    for r in row:
      sum+=r
    row.append(sum)
    matri.append(row)
  return matri

mat = [[1, 2], [3, 4]]
print(rowSum(mat))