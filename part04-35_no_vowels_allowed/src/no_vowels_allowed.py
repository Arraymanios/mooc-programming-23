# Write your solution here
def no_vowels(string):
  vowels = ['a','e','i','o','u']
  new_string = ""
  i = 0

  while i < len(string):
    if string[i] not in vowels:
      new_string += string[i]
    else:
      new_string += ""
    i += 1
  return new_string

if __name__ == "__main__":
  my_string = "this is an example"
  print(no_vowels(my_string))