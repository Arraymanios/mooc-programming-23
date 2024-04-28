# Write your solution here
def create_tuple(x: int, y: int, z: int):
  greatest = 0
  smallest = 0
  sum = x + y + z

  if x > y and x > z:
    greatest = x
  elif y > x and y > z:
    greatest = y
  elif z > x and z > y:
    greatest = z

  if x < y and x < z:
    smallest = x
  elif y < x and y < z:
    smallest = y
  elif z < x and z < y:
    smallest = z

  triple = (smallest, greatest, sum)
  return triple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
