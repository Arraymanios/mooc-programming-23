# Write your solution here
def palindromes(string):
  pal = True
  i = 0
  j = -1
  while i < len(string):
    if string[i] != string[j]:
      pal = False
      return pal
    i += 1
    j -= 1
  return pal

def type_palindrome():
  while True:
    pal = input("Please type in a palindrome: ")
    if palindromes(pal):
      print(f"{pal} is a palindrome!")
      break
    else:
      print("that wasn't a palindrome")


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
      
type_palindrome()
