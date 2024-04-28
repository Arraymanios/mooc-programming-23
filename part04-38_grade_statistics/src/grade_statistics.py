# Write your solution here

from math import floor
from operator import *

def results(): # storing and returning results for every student
  pair = [] # Containing grade at index 0 and nb of exercises at 1
  results = [] # Containing grades and nb of exercises of all students
  user_input = ""

  while True:
    user_input = input("Exam points and exercises completed: ")
    if user_input == "": # No empty inputs
      break
    pair = user_input.split(" ")
    if len(pair) != 2: # We want exactly two values
      break
    pair = [int(value) for value in pair]
    if 0 > pair[0] > 20 or 0 > pair[1] > 100: # Checking values match their respective intervals
      break
    results.append(pair[0])
    results.append(pair[1]) # Adding values two by two to results list

  return results

def statistics(list): # providing course's exams statistics
  print("Statistics:")
  i = 1
  sum = 0
  graduates = 0
  points = [] # storing total points (out of 30) for all students
  exam = [] # storing exam points of all students
  grade = [] # storing level of each student to calculate pass percentage
  
  while i < len(list):
    list[i] = floor(list[i] / 10) # calculating bonus points from exercises for each student
    i += 2
  
  i = 0

  while i < len(list) - 1:
    exam.append(list[i]) # retrieving exam points
    i += 2

  i = 0

  while i < len(list) - 1:
    points.append(list[i] + list[i+1]) # sum of exam and exercises points for each student
    i += 2 

  i = 0

  while i < len(points):
    sum += points[i]
    i += 1

  print(f"Points average: {sum/len(points):.1f}")

  i = 0

  while i < len(points): # ranking grades
    if exam[i] < 10:
      grade.append(0)
    elif points[i] <= 14:
      grade.append(0)
    elif 15 <= points[i] <= 17:
      grade.append(1)
    elif 18 <= points[i] <= 20:
      grade.append(2)
    elif 21 <= points[i] <= 23:
      grade.append(3)
    elif 24 <= points[i] <= 27:
      grade.append(4)
    elif 28 <= points[i] <= 30:
      grade.append(5)
    
    i += 1

  i = 0

  while i < len(grade): # Pass percentage = course's graduates proportion
    if grade[i] >= 1:
      graduates += 1
    i += 1

  print(f"Pass percentage: {100 * (graduates/len(grade)):.1f}")

  return grade

def grade_distribution(list):
  print("Grade distribution:")
  display = [0, 1, 2, 3, 4, 5]

  i = -1
  while i >= len(display)*(-1):
    print(f"{display[i]}: " + '*'*countOf(list, display[i])) # displaying the number of students that belong to each rank
    i -= 1

def main():

  res = results() # Using helper variables to call functions

  stat = statistics(res)

  grade_distribution(stat)

main()