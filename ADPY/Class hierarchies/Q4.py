import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            winner = self.round_winner(answer1, answer2)

            if winner == 1:
                self.wins1 += 1
                print("player 1 won")
            elif winner == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                print("It's a tie!")

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        return 0  

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def count_vowels(self, word: str):
        vowels = "aeiouAEIOU"
        return sum(1 for char in word if char in vowels)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels1 = self.count_vowels(player1_word)
        vowels2 = self.count_vowels(player2_word)

        if vowels1 > vowels2:
            return 1
        elif vowels1 < vowels2:
            return 2
        return 0

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_choices = {"rock", "paper", "scissors"}

        if player1_word not in valid_choices and player2_word not in valid_choices:
            return 0  
        elif player1_word not in valid_choices:
            return 2  
        elif player2_word not in valid_choices:
            return 1  

        if player1_word == player2_word:
            return 0  
        elif (player1_word == "rock" and player2_word == "scissors") or \
             (player1_word == "paper" and player2_word == "rock") or \
             (player1_word == "scissors" and player2_word == "paper"):
            return 1  
        else:
            return 2  


p = LongestWord(3)
p.play()
