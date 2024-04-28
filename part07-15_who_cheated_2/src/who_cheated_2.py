# Write your solution here
import csv

def hours_to_minutes(hour: str):
  time = hour.split(':')
  minutes = int(time[0]) * 60 + int(time[1])
  return minutes

def final_points():
  final_points = {}
  start_times = {}
  submissions = {}
  with open("start_times.csv", 'r') as file:
    for line in file:
      row = line.split(';')
      start_times[row[0]] = hours_to_minutes(row[1])
  with open("submissions.csv", 'r') as file2:
    for line in file2:
      row = line.split(';')
      name = row[0]
      exercise = row[1]
      points = row[2]
      submission = row[3]
      if name not in submissions:
        submissions[name] = {}
      if exercise not in submissions[name] or submissions[name][exercise][0] < points:
        submissions[name][exercise] = (points, hours_to_minutes(submission))
    for name in submissions:
      final_points[name] = 0
      for exercise in submissions[name]:
        points, submission = submissions[name][exercise]
        if (submission - start_times[name]) <= 180:
          final_points[name] += int(points)

  return final_points

if __name__ == "__main__":
  print(final_points())