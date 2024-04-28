# Write your solution here
import string

def change_case(orig_string: str):
  new_string = ""
  l = list(orig_string)
  for i in range(len(l)):
    if l[i].isupper():
      l[i] = l[i].lower()
    elif l[i].islower():
      l[i] = l[i].upper()
  new_string = ''.join(l)
  return new_string

def split_in_half(orig_string: str):
  first = orig_string[0:len(orig_string)//2]
  second = orig_string[len(orig_string)//2:]
  return (first, second)

def remove_special_characters(orig_string: str):
  special = ['§', '!', ':', '?', '¤', '*', ';', ',', '#', '%', '&', '(', ')', '/', '.', '_', '+', '=']
  new = []
  new_string = ""
  l = list(orig_string)
  for char in l:
    if char not in special:
      new.append(char)
  new_string = ''.join(new)
  return new_string


if __name__ == "__main__":
  print(change_case("Well hello there!"))
  print(split_in_half("This string is to be split in half."))
  print(split_in_half("abcd"))
  print(remove_special_characters("This is a test, lets see how it goes!!!11!"))