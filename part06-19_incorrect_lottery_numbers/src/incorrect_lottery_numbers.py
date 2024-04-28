# Write your solution here
def check_header(header: list):
  if(header[0]) != "week":
    print("String is not equal to 'week'")
    return -1
  elif type(header[1]) == "<class 'int'>" and header[1] <= 0:
    print("Week number is inferior or equal to zero")
    return -1
  elif type(header[1]) != "<class 'int'>":
    print("Week number not an integer")
    return -1
  return 0

def check_values(values: list):
  l = values
  while len(l) != 0:
    check = l[0]
    for i in range(1, len(l) - 1):
      if l[i] == check:
        print("Same number appears twice")
        return -1
    l.pop(0)
  for value in values:
    if len(values) != 7:
      print("List does not contain 7 values")
      return -1
    elif type(value) != "<class 'int'>":
      print("Value is not an integer")
      return -1
    elif value < 1 or value > 39:
      print("Value not between 1 and 39")
      return -1
  return 0
  
def filter_incorrect():
  with open("correct_numbers.csv", "w") as new_file:
    with open("lottery_numbers.csv", "r") as file:
      for line in file:
        lottery = line.split(';')
        header = lottery[0].split(' ')
        values = lottery[1].split(',')
        if(check_header(header) == 0 and check_values(values) == 0):
          new_file.write(line)

if __name__ == "__main__":
  filter_incorrect()