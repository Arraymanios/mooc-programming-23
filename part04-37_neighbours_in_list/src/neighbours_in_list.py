# Write your solution here
def longest_series_of_neighbours(list):
  length = 1
  max_length = 1

  for i in range(0, len(list) - 1):
    if abs(list[i] - list[i-1]) == 1:
      length += 1
    else:
      length = 1
    if length > max_length:
      max_length = length
  return max_length + 1

if __name__ == "__main__":
  list_1 = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
  list_2 = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25, 30]
  print(longest_series_of_neighbours(list_1))
  print(longest_series_of_neighbours(list_2))