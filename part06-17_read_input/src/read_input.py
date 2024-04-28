# Write your solution here
def read_input(usage: str, lower: int, upper: int):
  while True:
    try:
      number = int(input(usage))
      if lower <= number <= upper:
        return number
      else:
        print(f"You must type in an integer between {lower} and {upper}")
    except ValueError:
      print(f"You must type in an integer between {lower} and {upper}")

if __name__ == "__main__":
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)