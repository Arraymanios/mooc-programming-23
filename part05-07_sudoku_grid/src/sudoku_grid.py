# Write your solution here
def sudoku_grid_correct(sudoku: list):
  for i in range(9):
    if(row_correct(sudoku, i) == False):
        return False
    
  for i in range(9):
    if(column_correct(sudoku, i) == False):
        return False
    
  for i in range(0, 8, 3):
    for j in range(0, 8, 3):
      if(block_correct(sudoku, i, j) == False):
        return False
  
  return True

def row_correct(sudoku: list, row_no: int):
  values_checked = []
  for value in sudoku[row_no]:
    if value in values_checked:
      return False
    if value > 0:
      values_checked.append(value)
  return True

def column_correct(sudoku: list, column_no: int):
  values_checked = []
  for i in range(9):
    if sudoku[i][column_no] in values_checked:
      return False
    if sudoku[i][column_no] > 0:
      values_checked.append(sudoku[i][column_no])
  return True

def block_correct(sudoku: list, row_no: int, column_no: int):
  values_checked = []
  for i in range(row_no, row_no + 3):
    for j in range(column_no, column_no + 3):
      if sudoku[i][j] in values_checked:
        return False
      if sudoku[i][j] > 0:
        values_checked.append(sudoku[i][j])
      
  return True

if __name__ == "__main__":

  sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]

  print(sudoku_grid_correct(sudoku1))

  sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]]

  print(sudoku_grid_correct(sudoku2))