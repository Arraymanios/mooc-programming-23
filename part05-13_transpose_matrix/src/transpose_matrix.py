# Write your solution here
def transpose(matrix: list):
  for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
      if i != j:
        swap = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = swap

if __name__ == "__main__":

  m = [[1, 2, 3,], 
       [4, 5, 6], 
       [7, 8, 9]]

  transpose(m)
  print(m)