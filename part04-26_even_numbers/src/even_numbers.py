# Write your solution here
def even_numbers(list):
  even_nb_list = []
  for i in list:
    if i % 2 == 0:
      even_nb_list.append(i)
  return even_nb_list

if __name__ == "__main__":
  
  my_list = [-5, 3, 6, 7, 8, 12, 15, 9]

  print(even_numbers(my_list))