# Write your solution here

def filter_solutions():
  solution = []
  expression = []
  correct = []
  incorrect = []
  with open("solutions.csv", "r") as file:
    for line in file:
      solution = line.split(";")
      if '+' in solution[1]:
        expression = solution[1].split('+')
        operand = '+'
      elif '-' in solution[1]:
        expression = solution[1].split('-')
        operand = '-'
      result = int(solution [2])
      operator1 = int(expression[0])
      operator2 = int(expression[1])
      if operand == '+':
        if operator1 + operator2 == result:
          correct.append(line)
        else:
          incorrect.append(line)
      elif operand == '-':
        if operator1 - operator2 == result:
          correct.append(line)
        else:
          incorrect.append(line)
    with open("correct.csv", "w") as new_file:
      for element in correct:
        new_file.write(element)
      new_file.write("\n")
    with open("incorrect.csv", "w") as new_file_2:
      for element in incorrect:
        new_file_2.write(element)
      new_file_2.write("\n")

if __name__ == "__main__": 
  filter_solutions()
  filter_solutions()
  filter_solutions()
  print("Solutions:\n")
  with open("solutions.csv", "r") as file1:
    print(file1.read())
  print("Correct:\n")
  with open("correct.csv", "r") as file2:
    print(file2.read())
  print("Incorrect:\n")
  with open("incorrect.csv", "r") as file3:
    print(file3.read())