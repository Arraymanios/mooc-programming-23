# Write your solution here
def factorials(n: int):
  dictionary = {}
  j = 1
  for i in range(1, n+1):
    j = i * j
    dictionary[i] = j

  return dictionary


if __name__ == "__main__":

  k = factorials(5)
  print(k[1])
  print(k[3])
  print(k[5])