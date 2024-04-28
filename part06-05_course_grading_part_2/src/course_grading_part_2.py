# wwite your solution here
if True:
  student_info = input("Student information: ")
  exercise_data = input("Exercises completed: ")
  exam_points = input("Exam points: ")
else:
  student_info = "students1.csv"
  exercise_data = "exercises1.csv"
  exam_points = "exam_points1.csv"

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

exam_pts = {} 

with open(exam_points) as new_file:
  for line in new_file:
    parts = line.split(';')
    if parts[0] == "id":
      continue
    sum = 0
    for value in parts[1:]:
      sum += int(value)
    exam_pts[parts[0]] = sum

grades = {}

for id, exercise_amount in exercises.items():
  if id in exam_pts:
    grade = exam_pts[id] + ((exercise_amount * 100 // 40) // 10)
    if grade <= 14:
      grade = 0
    elif 15 <= grade <= 17:
      grade = 1
    elif 18 <= grade <= 20:
      grade = 2
    elif 21 <= grade <= 23:
      grade = 3
    elif 24 <= grade <= 27:
      grade = 4
    elif grade >= 28:
      grade = 5
    grades[id] = grade

for id, name in names.items():
  if id in grades:
    mark = grades[id]
    print(f"{name} {mark}\n", end="")