# Write your solution here
def shortest(list):
  best = list[0]
  for string in list:
    if len(string) < len(best):
      best = string
  return best

if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]

  result = shortest(my_list)
  print(result)