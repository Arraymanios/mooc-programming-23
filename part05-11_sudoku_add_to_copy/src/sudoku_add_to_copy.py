# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
  sudoku_copy = [] 
  for i in range(len(sudoku)): # for each inner list inside "sudoku" 
    tmp = [] # reinitializing temporary list to empty
    for value in sudoku[i]: 
      tmp.append(value) # each value from list number i is copied into temporary list
    sudoku_copy.append(tmp) # then the temporary list is integrated in sudoku's copy
  sudoku_copy[row_no][column_no] += number # adding a number to sudoku's copy
  return sudoku_copy

def print_sudoku(sudoku: list):
  for i in range(9):
    for j in range(9):
      if sudoku[i][j] <= 0:
        print("_ ", end = "")
      else:
        print(sudoku[i][j], "", end = "")
      if j == 2 or j == 5:
        print(" ", end = "")
    print()   
    if i == 2 or i == 5:
      print()


if __name__ == "__main__":
  sudoku  = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
  
  grid_copy = copy_and_add(sudoku, 1, 1, 2)
  print("Original:")
  print_sudoku(sudoku)
  print()
  print("Copy:")
  print_sudoku(grid_copy)