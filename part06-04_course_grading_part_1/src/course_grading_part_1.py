# write your solution here
if True:
  student_info = input("Student information: ")
  exercise_data = input("Exercises completed: ")
else:
  student_info = "students1.csv"
  exercise_data = "exercises1.csv"

names = {}

with open(student_info) as new_file:
  for line in new_file:
    parts = line.split(';')
    if parts[0] == "id":
      continue
    names[parts[0]] = (parts[1] + ' ' + parts[2]).rstrip()

exercises = {}

with open(exercise_data) as new_file:
  for line in new_file:
    parts = line.split(';')
    if parts[0] == "id":
      continue
    sum = 0
    for value in parts[1:]:
      sum += int(value)
    exercises[parts[0]] = sum

for id, name in names.items():
  if id in exercises:
    nb = exercises[id]
    print(f"{name} {nb}")