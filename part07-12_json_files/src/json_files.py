# Write your solution here
import json

def print_persons(filename: str):
  with open(filename) as file:
    students = json.load(file)
  
  for entry in students:
    hobbies = ', '.join(entry['hobbies'])
    print(f"{entry['name']} {entry['age']} years ({hobbies})")

if __name__ == "__main__":
  filename = input("Filename: ")
  print_persons(filename)