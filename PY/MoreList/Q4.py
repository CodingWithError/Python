def block_correct(sudoku,row_no,col_no):
  number=[]
  for i in range(row_no,row_no+3):
    for j in range(col_no,col_no+3):
      number.append(sudoku[i][j])
  non_zerono=[num for num in number if num!=0]
  return len(non_zerono)==len(set(non_zerono))


sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(block_correct(sudoku, 0, 0))  
print(block_correct(sudoku, 1, 2))