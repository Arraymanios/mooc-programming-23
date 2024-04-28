# Write your solution here
def new_person(name: str, age: int):
  if name == "":
    raise ValueError("Name is an empty string")
  elif len(name.split(" ")) < 2:
    raise ValueError("Name contains less than two words")
  elif len(name) > 40:
    raise ValueError("Name is longer than 40 characters")
  elif age < 0:
    raise ValueError("Age is a negative number")
  elif age > 150:
    raise ValueError("Age is greater than 150")
  
  data = (name, age)
  return data

if __name__ == "__main__":
  print(new_person("Ryuzaki Ryuga", 22))