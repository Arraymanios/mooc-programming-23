# Write your solution here
def list_sum(list1, list2):
  sum = []
  i = 0
  while i < len(list1):
    sum.append(list1[i] + list2[i])
    i += 1
  return sum

if __name__ == "__main__":
  l1 = [1, 2, 3]
  l2 = [5, 7, 9]

  print(list_sum(l1, l2))