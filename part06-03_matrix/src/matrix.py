# write your solution here
def matrix_sum():
  sum = 0
  with open("matrix.txt") as new_file:
    for line in new_file:
      line = line.replace("\n", "")
      row = line.split(",")
      for value in row:
        sum += int(value)
  return sum

def matrix_max():
  max = 0
  with open("matrix.txt") as new_file:
    for line in new_file:
      line = line.replace("\n", "")
      row = line.split(",")
      for value in row:
        if int(value) > max:
          max = int(value)
  return max

def row_sums():
  row_sums = []
  with open("matrix.txt") as new_file:
    for line in new_file:
      sum = 0
      line = line.replace("\n", "")
      row = line.split(",")
      for value in row:
        sum += int(value)
      row_sums.append(sum)
  return row_sums

if __name__ == "__main__":
  print("matrix sum :")
  print(matrix_sum())
  print("matrix max :")
  print(matrix_max())
  print("row sums :")
  print(row_sums())