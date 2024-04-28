# Write your solution here
def length_of_longest(list):
  best = ""
  for string in list:
    if len(string) > len(best):
      best = string
  return len(best)

if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]

  result = length_of_longest(my_list)
  print(result)