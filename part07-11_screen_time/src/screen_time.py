# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
starting = input("Starting date: ")
nb_days = int(input("How many days: "))
start_date = datetime.strptime(starting, "%d.%m.%Y")
period = f"Time period: {start_date.date().strftime('%d.%m.%Y')}-{(start_date + timedelta(days = nb_days)).date().strftime('%d.%m.%Y')}\n"
i = 0
total_time = 0
average_time = 0
detail = ""
daily_time = []

print("Please type in screen time in minutes on each day (TV computer mobile):")

while i < nb_days:
  screen_time = input(f"Screen time {(start_date + timedelta(days=i)).date().strftime('%d.%m.%Y')}: ")
  daily_time = screen_time.split(' ')
  for value in daily_time:
    total_time += int(value)
  detail += f"{(start_date + timedelta(days=i)).date().strftime('%d.%m.%Y')}: " + f"{daily_time[0]}/{daily_time[1]}/{daily_time[2]}\n"
  i += 1
average_time = total_time / i
with open(filename, 'w') as file:
  file.write(period)
  file.write(f"Total minutes: {total_time}\n")
  file.write(f"Average minutes: {average_time:.1f}\n")
  file.write(detail)

print(f"Data stored in file {filename}")

with open(filename, 'r') as file:
  print(file.read())