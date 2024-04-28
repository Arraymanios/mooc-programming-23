# Write your solution here

def length_of_longest(list):
  best = ""
  for string in list:
    if len(string) > len(best):
      best = string
  return len(best)

def all_the_longest(list):
  new_list = []
  for string in list:
    if len(string) >= length_of_longest(list):
      new_list.append(string)
  return new_list

if __name__ == "__main__":
  my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

  result = all_the_longest(my_list)
  print(result) # ['dorothy', 'richard']

