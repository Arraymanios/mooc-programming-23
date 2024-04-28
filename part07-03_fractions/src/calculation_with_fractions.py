# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
  fract = []
  for i in range(amount):
    fract.append(Fraction(1, amount))

  return fract

if __name__ == "__main__":
  for f in fractionate(4):
    print(f)

  print()
  print(fractionate(2))