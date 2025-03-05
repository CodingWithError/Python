def play_turn(game_board: list,no: int,no1: int,no2: int):
  game_board[no][no1]=no2


game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
play_turn(game_board, 0, 2, "X")
print(game_board)