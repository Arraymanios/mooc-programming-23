# Write your solution here
from random import *

def words(n: int, beginning: str):
  word = ""
  word_list = []
  random_list = []
  i = 0
  with open("words.txt", "r") as file:
    for word in file:
      random_list.append(word)
    while True:
      if len(word_list) == n:
        break
      match = True
      word = choice(random_list)
      if len(word) < len(beginning):
        match = False
      else:
        for i in range(len(beginning)):
          if word[i] != beginning[i]:
            match = False
      if match and word not in word_list:
        word_list.append(word)
  if len(word_list) < n:
    raise ValueError("Not enough words")
  return word_list

if __name__ == "__main__":
  word_list = words(10, "car")
  print(word_list)