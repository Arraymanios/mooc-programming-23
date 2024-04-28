# Write your solution here
from string import *

def separate_characters(my_string: str):
  letters = ""
  punct = ""
  others = ""

  for character in my_string:
    if character in ascii_letters:
      letters += character
    elif character in punctuation:
      punct += character
    else:
      others += character

  char = (letters, punct, others)

  return char

if __name__ == "__main__":
  parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
  print(parts[0])
  print(parts[1])
  print(parts[2])