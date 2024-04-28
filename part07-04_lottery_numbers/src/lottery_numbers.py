# Write your solution here
from random import *

def lottery_numbers(amount: int, lower: int, upper: int):
  lottery = []

  while len(lottery) < amount:
    rand_nb = randint(lower, upper)
    if rand_nb not in lottery:
      lottery.append(rand_nb)

  lottery.sort()
  return lottery

if __name__ == "__main__":
  for nb in lottery_numbers(7, 1, 40):
    print(nb)