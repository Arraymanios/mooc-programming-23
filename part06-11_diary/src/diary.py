# Write your solution here
while True:
  print("1 - add an entry, 2 - read entries, 0 - quit")
  function = int(input("Function: "))
  if function == 1:
    string = input("Diary entry: ") + '\n'
    with open("diary.txt", "a") as my_file:
      my_file.write(string)
    print("Diary saved")
  elif function == 2:
    print("Entries:")
    with open("diary.txt") as my_file:
      for line in my_file:
        print(line)
  elif function == 0:
    print("Bye now!")
    break
