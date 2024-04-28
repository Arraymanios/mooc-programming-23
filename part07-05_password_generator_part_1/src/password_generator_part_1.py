# Write your solution here
from random import *

def generate_password(length: int):
  password = ""
  while len(password) < length:
    password += chr(randint(97, 122))
  return password


if __name__ == "__main__":
  for i in range(9):
    print(generate_password(19))