# Write your solution here
def most_common_character(string):
  max = 0
  for i in string:
    if string.count(i) > max:
      max = string.count(i)
  for i in string:
    if string.count(i) == max:
      return i
    
if __name__ == "__main__":
  first_string = "abcdbde"
  print(most_common_character(first_string))

  second_string = "exemplaryelementary"
  print(most_common_character(second_string))