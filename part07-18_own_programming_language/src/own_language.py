# Write your solution here

def run(program: list):
  output = []
  variables_list = []
  mnemonics = ["PRINT", "MOV", "ADD", "SUB", "MUL", "JUMP", "IF"]
  variables = {}
  locations = {}

  for i in range(65, 91):
    variables[chr(i)] = 0

  variables_list = list(variables.keys())

  i = 0
  while i < len(program):
    parts = program[i].split(' ')
    if parts[0] not in mnemonics:
      locations[parts[0]] = i
    i += 1

  i = 0
  while i < len(program):
    parts = program[i].split(' ')

    if parts[0] == "PRINT":
      if parts[1] in variables_list:
        output.append(variables[parts[1]])
      else:
        output.append(int(parts[1]))
    elif parts[0] == "MOV":
      if parts[2] in variables_list:
        variables[parts[1]] = variables[parts[2]]
      else:
        variables[parts[1]] = int(parts[2])
    elif parts[0] == "ADD":
      if parts[2] in variables_list:
        variables[parts[1]] += variables[parts[2]]
      else:
        variables[parts[1]] += int(parts[2])
    elif parts[0] == "SUB":
      if parts[2] in variables_list:
        variables[parts[1]] -= variables[parts[2]]
      else:
        variables[parts[1]] -= int(parts[2])
    elif parts[0] == "MUL":
      if parts[2] in variables_list:
        variables[parts[1]] *= variables[parts[2]]
      else:
        variables[parts[1]] *= int(parts[2])
    elif parts[0] == "JUMP":
      i = locations[f"{parts[1]}" + ':']
      continue 
    elif parts[0] == "IF":
      if parts[1] in variables and parts[3] in variables:
        operand1 = variables[parts[1]]
        operand2 = variables[parts[3]]
      elif parts[1] in variables:
        operand1 = variables[parts[1]]
        operand2 = int(parts[3])
      elif parts[3] in variables:
        operand1 = int(parts[1])
        operand2 = variables[parts[3]]
      if parts[2] == "==":
        if(operand1 == operand2):
          i = locations[f"{parts[5]}" + ':']
          continue
      elif parts[2] == "!=":
        if(operand1 != operand2):
          i = locations[f"{parts[5]}" + ':']
          continue
      elif parts[2] == "<":
        if(operand1 < operand2):
          i = locations[f"{parts[5]}" + ':']
          continue
      elif parts[2] == "<=":
        if(operand1 <= operand2):
          i = locations[f"{parts[5]}" + ':']
          continue
      elif parts[2] == ">":
        if(operand1 > operand2):
          i = locations[f"{parts[5]}" + ':']
          continue
      elif parts[2] == ">=":
        if(operand1 >= operand2):
          i = locations[f"{parts[5]}" + ':']
          continue
      elif parts[0] == "END":
        break

    i += 1

  return output

if __name__ == "__main__":
  program4 = []
  program4.append("MOV N 50")
  program4.append("PRINT 2")
  program4.append("MOV A 3")
  program4.append("begin:")
  program4.append("MOV B 2")
  program4.append("MOV Z 0")
  program4.append("test:")
  program4.append("MOV C B")
  program4.append("new:")
  program4.append("IF C == A JUMP error")
  program4.append("IF C > A JUMP over")
  program4.append("ADD C B")
  program4.append("JUMP new")
  program4.append("error:")
  program4.append("MOV Z 1")
  program4.append("JUMP over2")
  program4.append("over:")
  program4.append("ADD B 1")
  program4.append("IF B < A JUMP test")
  program4.append("over2:")
  program4.append("IF Z == 1 JUMP over3")
  program4.append("PRINT A")
  program4.append("over3:")
  program4.append("ADD A 1")
  program4.append("IF A <= N JUMP begin")
  result = run(program4)
  print(result)