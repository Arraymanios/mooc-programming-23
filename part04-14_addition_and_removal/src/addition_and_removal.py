# Write your solution here
my_list = []
choice = ''

print(f"The list is now {my_list}")
while True:
  choice = input("a(d)d, (r)emove or e(x)it:")
  if choice == 'x':
    print("Bye!")
    break
  elif choice == 'd':
    if(len(my_list) >= 1):
      value = my_list[len(my_list) - 1] + 1
    else:
      value = 1   
    my_list.append(value)
  elif choice == 'r':
    my_list.pop(len(my_list) - 1)
  print(f"The list is now {my_list}")