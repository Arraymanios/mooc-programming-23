# Write your solution here
import urllib.request, json, math

def retrieve_all():
  courses = []
  request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
  content = json.loads(request.read())  # Lire le contenu de la réponse HTTP
  for course in content:
    fullName = ""
    name = ""
    year = ""
    exercises = 0
    if course['enabled'] == True:
      fullName = course['fullName']
      name = course['name']
      year = course['year']
      for value in course['exercises']:
        exercises += value
      courses.append((fullName, name, year, exercises))
      
  return courses

def retrieve_course(course_name: str):
  statistics = {}
  weeks = 0
  students = 0
  hours = 0
  hours_average = 0
  exercises = 0
  exercises_average = 0
  request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
  content = json.loads(request.read())
  weeks = len(content)
  for week in content.values():  # Itérer sur les valeurs du dictionnaire
    if 'students' in week:
      students = max(students, week['students'])
    if 'hour_total' in week:
      hours += week['hour_total']
    if 'exercise_total' in week:
      exercises += week['exercise_total']
  if students > 0:
    hours_average = round(hours // students)
    exercises_average = round(exercises // students)
  statistics['weeks'] = weeks
  statistics['students'] = students
  statistics['hours'] = hours
  statistics['hours_average'] = hours_average
  statistics['exercises'] = exercises
  statistics['exercises_average'] = exercises_average
  
  return statistics

if __name__ == "__main__":
  print(retrieve_all())
  print(retrieve_course("docker2019"))