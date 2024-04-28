# Write your solution here
from random import *

def roll(die: str):
  A = [3, 3, 3, 3, 3, 6]
  B = [2, 2, 2, 5, 5, 5]
  C = [1, 4, 4, 4, 4, 4]
  
  if die == 'A':
    return choice(A)
  elif die == 'B':
    return choice(B)
  elif die == 'C':
    return choice(C)
  
def play(die1 : str, die2: str, times: int):
  one_wins = 0
  two_wins = 0
  ties = 0

  for i in range(times):
    roll1 = roll(die1)
    roll2 = roll(die2)
    if roll1 > roll2:
      one_wins += 1
    elif roll1 < roll2:
      two_wins += 1
    elif roll1 == roll2:
      ties += 1
  results = (one_wins, two_wins, ties)
  return results

if __name__ == "__main__":
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