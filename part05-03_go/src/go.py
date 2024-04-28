# Write your solution here
def who_won(game_board: list):
  nb_of_1 = 0
  nb_of_2 = 0
  for row in game_board:
    for value in row:
      if value == 1:
        nb_of_1 += 1
      elif value == 2:
        nb_of_2 += 1
  if nb_of_1 > nb_of_2:
    return 1
  elif nb_of_2 > nb_of_1:
    return 2
  elif nb_of_1 == nb_of_2:
    return 0
