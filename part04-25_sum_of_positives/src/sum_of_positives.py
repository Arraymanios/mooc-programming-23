# Write your solution here
def sum_of_positives(list):
  sum = 0
  for i in list:
    if i > 0:
      sum += i
  return sum

if __name__ == "__main__":
  
  my_list = [-5, 3, 6, 9]

  print(sum_of_positives(my_list))