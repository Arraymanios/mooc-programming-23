# Write your solution here

def add_student(students: dict, name: str):
  if name in students :
    print(f"Student {name} already exists in database")
  else :
    students[name] = []

def print_student(students: dict, name: str):
  if name in students:
    nb = len(students[name])
    sum = 0
    if nb == 0:
      print(f"{name}:\n no completed courses")
    else:
      print(f"{name}:\n {nb} completed courses:\n")
      for course, grade in students[name]:
        print(f"{course} {grade}")
        sum += grade
      print(f"average grade {sum/nb}")
  else:
    print(f"{name}: no such person in the database")
    

def add_course(students: dict, name: str, course: tuple):
  (course_name, grade) = course
  if name in students: 
      for i, existing_course in enumerate(students[name]): # checking for each matching course name tuple if the argument tuple's grade is superior, if so the current tuple is replaced
          if existing_course[0] == course_name:
              if grade > existing_course[1]:
                    students[name][i] = (course_name, grade)
              return
      students[name].append((course_name, grade)) # if the course doesn't exist within the list the argument tuple is added to it

def summary(students: dict):
  avg = 0 
  best_avg = 0 
  completed = 0
  best_student = "" 
  most_completed = ""
  print(f"students {len(students)}\n most courses completed {completed} {most_completed}\n best average grade {best_avg} {best_student}")

if __name__ == "__main__":
  students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
add_course(students, "Peter", ("Data Structures and Algorithms", 1))
add_course(students, "Peter", ("Introduction to Programming", 1))
add_course(students, "Peter", ("Advanced Course in Programming", 1))
add_course(students, "Eliza", ("Introduction to Programming", 5))
add_course(students, "Eliza", ("Introduction to Computer Science", 4))
summary(students)