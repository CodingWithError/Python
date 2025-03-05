import random
def roll(die: str):
    dice = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
    return random.choice(dice[die])

def play(die1,die2,time):
  win_die1, win_die2, ties=0,0,0

  for _ in range(time):
    roll1=roll(die1)
    roll2=roll(die2)

    if roll1>roll2:
      win_die1+=1
    elif roll2>roll1:
       win_die2+=1
    else:
       ties+=1
  
  return (win_die1,win_die2,ties)
      

for i in range(20):
    print(roll("A"), " ", end="")
print()
for i in range(20):
    print(roll("B"), " ", end="")
print()
for i in range(20):
    print(roll("C"), " ", end="")
print()

result = play("A", "C", 1000)
print(result)
result = play("B", "B", 1000)
print(result)