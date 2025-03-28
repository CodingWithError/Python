class ComputerGame:
    def __init__(self, name: str, developer: str, year: int):
        self.name = name
        self.developer = developer
        self.year = year

class GameWarehouse:
    def __init__(self):
        self._games = []

    def add_game(self, game: ComputerGame): 
        self._games.append(game)

    def list_games(self):
        return self._games

class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        return [game for game in self._games if game.year < 1990]
  

museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
for game in museum.list_games():
    print(game.name)