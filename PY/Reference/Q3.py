sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
def change(sudoku: list):
  for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
      if sudoku[i][j]==0:
        sudoku[i][j]='_'
  return sudoku

def add_number(sudoku: list,no: int,no1: int,no2: int):
  sudoku[no][no1]=no2


sudoku=change(sudoku)
print(sudoku)

add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print(sudoku)
