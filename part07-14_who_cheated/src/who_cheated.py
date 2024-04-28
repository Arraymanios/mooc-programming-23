# Write your solution here
import csv

def hours_to_minutes(hour: str):
  time = hour.split(':')
  minutes = int(time[0]) * 60 + int(time[1])
  return minutes

def cheaters():
  cheaters = []
  start_times = {}
  with open("start_times.csv", 'r') as file:
    for line in file:
      row = line.split(';')
      start_times[row[0]] = hours_to_minutes(row[1]) # storing "start_times.csv" content
    
  with open("submissions.csv", 'r') as file2:
    for line in file2:
      row = line.split(';')
      if(hours_to_minutes(row[3]) - start_times[row[0]]) > 180: # checking if difference between starting time and submission superior to 180 minutes (3 hours)
        if row[0] not in cheaters: # avoiding doubles
          cheaters.append(row[0])

  return cheaters

if __name__ == "__main__":
  print(cheaters())