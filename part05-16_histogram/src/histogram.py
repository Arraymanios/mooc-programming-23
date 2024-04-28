# Write your solution here
def histogram(string: str):
  occurences = {}

  for letter in string:
    if letter not in occurences:
      occurences[letter] = 0
    occurences[letter] += 1

  for key in occurences:
    print(f"{key}", "*"*occurences[key])

if __name__ == "__main__":
  histogram("statistically")