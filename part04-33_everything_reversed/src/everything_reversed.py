# Write your solution here

def reverse_string(string):
  return string[::-1]

def everything_reversed(list):
  new_list = []
  i = len(list) - 1
  while i >= 0:
    new_list.append(reverse_string(list[i]))
    i -= 1
  return new_list

if __name__ == "__main__":
  my_list = ["Hi", "there", "example", "one more"]
  new_list = everything_reversed(my_list)
  print(new_list)


