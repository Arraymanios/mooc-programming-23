# Write your solution here
def row_correct(sudoku: list, row_no: int):
  values_checked = []
  for value in sudoku[row_no]:
    if value in values_checked:
      return False
    if value > 0:
      values_checked.append(value)
  return True

if __name__ == "__main__":
  
  sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [3, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]

  print(row_correct(sudoku, 2))